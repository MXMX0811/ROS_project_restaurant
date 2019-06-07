#!/usr/bin/env python

import sys
import rospy
from turtlebot_msgs.srv import SetFollowState

def follower_client(msg):
    rospy.wait_for_service('/turtlebot_follower/change_state')
    try:
        change_state = rospy.ServiceProxy('/turtlebot_follower/change_state', SetFollowState)
	return change_state(msg)
    except rospy.ServiceException, e:
        print "Service call failed: %s" % e

def keyboard_control():
    command = ' '
    while command !='q':
        try:
            command = raw_input('please enter the command:')
            if command == 'f':
                follower_client(1)
            if command == 's':
                follower_client(0)
            else:
                print("invalid input!")
        except EOFError:
            print "Error!"

if __name__ == "__main__":
    keyboard_control()
