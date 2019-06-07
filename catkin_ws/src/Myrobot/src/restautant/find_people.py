#!/usr/bin/env python
# encoding: utf-8

import rospy
import time
from std_msgs.msg import String
from geometry_msgs.msg import Twist
#from tf_conversions import transformations
from tf import transformations
from math import pi
import tf
from std_msgs.msg import Float64

width = 640
height = 480
left = width / 2 - width / 10
right = width / 2 + width / 10
top = height / 2 - height / 10
bottom = height / 2 + height / 10
Kz = .003
Kx = .001
height_body = 0
error_x = 0
x_OK = 0
y_OK = 0

class Robot:
    def __init__(self):
        self.tf_listener = tf.TransformListener()
        try:
            self.tf_listener.waitForTransform('/map', '/base_link', rospy.Time(), rospy.Duration(1.0))
        except (tf.Exception, tf.ConnectivityException, tf.LookupException):
            return

    def get_pos(self):
        try:
            (trans, rot) = self.tf_listener.lookupTransform('/map', '/base_link', rospy.Time(0))
        except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
            #rospy.loginfo("tf Error")
            return None
        euler = transformations.euler_from_quaternion(rot)
        #print euler[2] / pi * 180

        x = trans[0]
        y = trans[1]
        th = euler[2] / pi * 180
        pos = [x,y,th]
        return pos
    
def body_callback(data):
	rate = rospy.Rate(10)
	pub = rospy.Publisher('/cmd_vel_mux/input/navi', Twist, queue_size=5)
	global height_body
	twi = Twist()
	height_body = float(data.data)
	print(height_body)
	if height_body > bottom:
		twi.linear.x = Kx * (height_body - height / 2)
		print(twi.linear.x)
		pub.publish(twi)
		rate.sleep()
	elif height < top:
		twi.linear.x = Kx * (height_body - height / 2)
		print(twi.linear.x)
		pub.publish(twi)
		rate.sleep()
	else:
		global x_OK, y_OK
		y_OK = 1
		if x_OK == 1 and y_OK == 1:
			pub_start_pos = rospy.Publisher('start_pos', String, queue_size=1)
			print('OK!')
			robot = Robot()
			while 1:
				if robot.get_pos():
					start_pos = robot.get_pos()
					print(start_pos)
					pub_start_pos.publish(str(start_pos[0])+','+str(start_pos[1])+','+str(start_pos[2]))
					break
			pub_finish.publish('finding_finish')
			time.sleep(0.5)
			rospy.signal_shutdown('finish!')


def body_error_callback(data):
	rate = rospy.Rate(10)
	pub = rospy.Publisher('/cmd_vel_mux/input/navi', Twist, queue_size=5)
	global error_x
	twi = Twist()
	error_x = float(data.data)
	if error_x < left:
		twi.angular.z = - Kz * (error_x - width / 2)
		print(twi.angular.z)
		pub.publish(twi)
		rate.sleep()
	elif error_x > right:
		twi.angular.z = - Kz * (error_x - width / 2)
		print(twi.angular.z)
		pub.publish(twi)
		rate.sleep()
	else:
		global x_OK, y_OK
		x_OK = 1
		if x_OK == 1 and y_OK == 1:
			pub_start_pos = rospy.Publisher('start_pos', String, queue_size=1)
			print('OK!')
			robot = Robot()
			while 1:
				if robot.get_pos():
					start_pos = robot.get_pos()
					print(start_pos)
					pub_start_pos.publish(str(start_pos[0])+','+str(start_pos[1])+','+str(start_pos[2]))
					break
			pub_finish.publish('finding_finish')
			time.sleep(0.5)
			rospy.signal_shutdown('finish!')



if __name__ == '__main__':
	rospy.init_node('find_people', anonymous=True)
	pub_finish = rospy.Publisher('finding_finish', String, queue_size=1)
	rospy.wait_for_message('start_find', String)	#接收到开始寻找目标人的信息

	rospy.Subscriber('body_x_error', String, body_error_callback)
	rospy.Subscriber('body_height', String, body_callback)

	print('Start finding')
	

	rospy.spin()

