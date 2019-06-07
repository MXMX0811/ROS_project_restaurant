#!/usr/bin/env python

"""
    arm.py - move robot arm according to predefined gestures

"""

import rospy
from std_msgs.msg import Float64
from std_msgs.msg import String
import time

class Loop:
    def __init__(self):
        rospy.on_shutdown(self.cleanup)

	# publish command message to joints/servos of arm
    	self.joint1 = rospy.Publisher('/waist_controller/command',Float64)
	self.joint2 = rospy.Publisher('/shoulder_controller/command',Float64)
    	self.joint3 = rospy.Publisher('/elbow_controller/command',Float64)
    	self.joint4 = rospy.Publisher('/wrist_controller/command',Float64)
	self.joint5 = rospy.Publisher('/hand_controller/command',Float64)
	self.pos1 = Float64()
    	self.pos2 = Float64()
    	self.pos3 = Float64()
    	self.pos4 = Float64()
    	self.pos5 = Float64()
	
	# Initial gesture of robot arm
	self.pos1 = 0.0
	self.pos2 = -2.09
	self.pos3 = 2.4
	self.pos4 = 1.04
	self.pos5 = -0.4
	self.joint1.publish(self.pos1)
	self.joint2.publish(self.pos2)
	self.joint3.publish(self.pos3)
	self.joint4.publish(self.pos4)
	self.joint5.publish(self.pos5)

	pub = rospy.Publisher('arm2navi', String, queue_size=1)

	while not rospy.is_shutdown():
		time.sleep(2)
		# gesture 1
		self.pos1 = 0.0
		self.pos2 = -2.09
		self.pos3 = 2.61
		time.sleep(5)
		self.pos4 = 1.04
		self.pos5 = -0.4
		self.joint1.publish(self.pos1)
		self.joint2.publish(self.pos2)
		self.joint3.publish(self.pos3)
		self.joint4.publish(self.pos4)
		self.joint5.publish(self.pos5)

		rospy.wait_for_message('nav2arm', String)
		
		# gesture 2
		self.pos1 = 0.0
		self.pos2 = 2.09
		self.pos3 = 2.09
		self.pos4 = -0.57
		self.pos5 = -0.4
		self.joint4.publish(self.pos4)
		self.joint1.publish(self.pos1)
		self.joint2.publish(self.pos2)
		self.joint3.publish(self.pos3)
		self.joint5.publish(self.pos5)
		time.sleep(15)
		self.pos3 = 0.0
		self.joint3.publish(self.pos3)
		time.sleep(10)
		self.pos5 = 0.4
		self.joint5.publish(self.pos5)
		time.sleep(5)
		self.joint4.publish(-0.9)
		pub.publish('arm2navi')
		rospy.wait_for_message('navi_finish', String)
		print('countinue')

		# gesture 3
		self.pos1 = 0.0
		self.pos2 = 0.52
		self.pos3 = 0.0
		self.pos4 = 0.52
		self.pos5 = 0.2
		self.joint1.publish(self.pos1)
		self.joint2.publish(self.pos2)
		self.joint4.publish(self.pos4)
		self.joint3.publish(self.pos3)
		time.sleep(10)
		self.joint5.publish(self.pos5)
		rospy.sleep(3)
		break


		
    def cleanup(self):
        rospy.loginfo("Shutting down robot arm....")

if __name__=="__main__":
    rospy.init_node('arm')
    try:
        Loop()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass

