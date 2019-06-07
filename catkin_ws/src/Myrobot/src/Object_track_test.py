#!/usr/bin/env python
# -*- coding: utf-8 -*-

import dlib
import cv2
import time
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist

X = 0
Y = 0
width = 640
height = 480
left = width / 2 - width / 12
right = width / 2 + width / 12
top = height / 2 - height / 12
bottom = height / 2 + height / 12
Kz = .003
Kx = .0005

def callback_x(data):
	twi = Twist()
	#rospy.loginfo('x: %s',data.data)
	X = float(data.data)
	if X < left:
		twi.angular.z = Kz * (X - width / 2)
		pub.publish(twi)
	elif X > right:
		twi.angular.z = Kz * (X - width / 2)
		pub.publish(twi)
    
            
def callback_y(data):
	twi = Twist()
	#rospy.loginfo('y: %s',data.data)
	Y = float(data.data)
	if Y > bottom:
		twi.linear.x = Kx * (Y - height / 2)
		pub.publish(twi)
	elif Y < top:
		twi.linear.x = Kx * (Y - height / 2)
		pub.publish(twi)
	


def keyboard_control():
	command = ''
	while command != 'c':
		try:
			command = raw_input('next command : ')
			if command == 'r':
				read_capture()
			else:
				print("Invalid Command!")
		except Exception as e:
			print e


rospy.init_node("track_object")
pub = rospy.Publisher('//cmd_vel_mux/input/navi', Twist, queue_size=5)
sub_x = rospy.Subscriber('/camshift/track_box_test_x', String, callback_x)
sub_y = rospy.Subscriber('/camshift/track_box_test_y', String, callback_y)

keyboard_control()


