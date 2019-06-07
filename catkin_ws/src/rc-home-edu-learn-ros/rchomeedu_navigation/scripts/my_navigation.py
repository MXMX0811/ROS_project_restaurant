#!/usr/bin/env python
# encoding: utf-8
"""

    RoboCup@Home Education | oc@robocupathomeedu.org
    navi.py - enable turtlebot to navigate to predefined waypoint location

"""

import rospy
from std_msgs.msg import String
from std_msgs.msg import Float64
import actionlib
from actionlib_msgs.msg import *
from geometry_msgs.msg import Pose, PoseWithCovarianceStamped, Point, Quaternion, Twist
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from tf.transformations import quaternion_from_euler

original = 0
start = 1
# Default Location A
A_x = 0
A_y = 0
A_theta = 0


class NavToPoint:
	

	def __init__(self):
		rospy.on_shutdown(self.cleanup)
		
	# Subscribe to the move_base action server
		self.move_base = actionlib.SimpleActionClient("move_base", MoveBaseAction)

		rospy.loginfo("Waiting for move_base action server...")

		global A_x, A_y, A_theta, start, original

		# Wait for the action server to become available
		self.move_base.wait_for_server(rospy.Duration(120))
		rospy.loginfo("Connected to move base server")

		# A variable to hold the initial pose of the robot to be set by the user in RViz
		initial_pose = PoseWithCovarianceStamped()
		rospy.Subscriber('initialpose', PoseWithCovarianceStamped, self.update_initial_pose)

	# Get the initial pose from the user
		rospy.loginfo("*** Click the 2D Pose Estimate button in RViz to set the robot's initial pose...")
		rospy.wait_for_message('initialpose', PoseWithCovarianceStamped)
		
		# Make sure we have the initial pose
		while initial_pose.header.stamp == "":
			rospy.sleep(1)
			
		rospy.loginfo("Ready to go")
		rospy.sleep(1)

		locations = dict()

		while A_x == 0 and A_y == 0 and A_theta == 0:
			print(A_x,A_y,A_theta)
			rospy.Subscriber('start_pos', String, self.get_start_pose)

		# Location B
		B_x = -4.001
		B_y = -0.982
		B_theta = 2.597

		quaternion_A = quaternion_from_euler(0.0, 0.0, A_theta)
		locations['A'] = Pose(Point(A_x, A_y, 0.000), Quaternion(quaternion_A[0], quaternion_A[1], quaternion_A[2], quaternion_A[3]))

		quaternion_B = quaternion_from_euler(0.0, 0.0, B_theta)
		locations['B'] = Pose(Point(B_x, B_y, 0.000), Quaternion(quaternion_B[0], quaternion_B[1], quaternion_B[2], quaternion_B[3]))

		self.goal = MoveBaseGoal()
		rospy.loginfo("Starting navigation test")


		while not rospy.is_shutdown():
			self.goal.target_pose.header.frame_id = 'map'
			self.goal.target_pose.header.stamp = rospy.Time.now()
			rospy.wait_for_message('start_navi', String)	#接收消息，是否开始导航

		# Robot will go to point B
			if start == 1:
				pub = rospy.Publisher('catch_start', String, queue_size=10)
				rospy.loginfo("Going to point B")
				rospy.sleep(2)
				self.goal.target_pose.pose = locations['B']
				self.move_base.send_goal(self.goal)
				waiting = self.move_base.wait_for_result(rospy.Duration(300))
				if waiting == 1:
					rospy.loginfo("Reached point B")
					rospy.sleep(2)
					rospy.loginfo("Ready to go back")
					rospy.sleep(2)
					global start
					start = 0
					pub.publish('ready_to_catch') 	#向抓取的节点发布消息，使其开始
					rospy.wait_for_message('arm2navi', String)	#抓取结束后继续

		# Robot will go to point A
			if start == 0:
				pub = rospy.Publisher('navi_finish', String, queue_size=10)
				rospy.loginfo("Going to point A")
				rospy.sleep(2)
				self.goal.target_pose.pose = locations['A']
				self.move_base.send_goal(self.goal)
				waiting = self.move_base.wait_for_result(rospy.Duration(300))
				if waiting == 1:
					rospy.loginfo("Reached point A")
					rospy.sleep(2)
					rospy.loginfo("Ready to go back")
					rospy.sleep(2)
					global start
					start = 2
					pub.publish('navi_finish')
					break
			rospy.Rate(5).sleep()

	def update_initial_pose(self, initial_pose):
		self.initial_pose = initial_pose
		if original == 0:
			self.origin = self.initial_pose.pose.pose
			global original
			original = 1

	def get_start_pose(self, start_pose):
		global A_x, A_y, A_theta
		pose = start_pose.data.split(',')
		A_x = float(pose[0])
		A_y = float(pose[1])
		A_theta = float(pose[2])

	def cleanup(self):
		rospy.loginfo("Shutting down navigation	....")
		self.move_base.cancel_goal()

if __name__=="__main__":
	rospy.init_node('navi_point')
	try:
		NavToPoint()
		rospy.spin()
	except:
		pass

