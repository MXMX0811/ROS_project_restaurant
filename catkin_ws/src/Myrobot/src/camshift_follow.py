#!/usr/bin/env python
# -*- coding: utf-8 -*-

import dlib
import cv2
import time
import rospy
from opencv_apps.msg import RotatedRectStamped
from std_msgs.msg import String
from geometry_msgs.msg import Twist


class camshift_follow():
    def __init__(self):
        rospy.init_node("find_object")
        self.pub = rospy.Publisher('//cmd_vel_mux/input/navi', Twist, queue_size=5)
        self.sub = rospy.Subscriber('/camshift/track_box', RotatedRectStamped, self.call_back)
        self.X = self.Y = 0
        self.cam_width = 640
        self.cam_height = 480
        self.left = self.cam_width / 2 - self.cam_width / 12
        self.right = self.cam_width / 2 + self.cam_width / 12
        self.top = self.cam_height / 2 - self.cam_height / 12
        self.bottom = self.cam_height / 2 + self.cam_height / 12
        self.Kz = .003
        self.Kx = .0005
        self.keyboard_control()


    def call_back(self,msg):
        twi = Twist()
        X = msg.rect.center.x
        Y = msg.rect.center.y
        if X < self.left:
            twi.angular.z = self.Kz * (X - self.cam_width / 2)
            self.pub.publish(twi)
            print twi
        elif X > self.right:
            twi.angular.z = self.Kz * (X - self.cam_width / 2)
            self.pub.publish(twi)
            print twi

        if Y > self.bottom:
            twi.linear.x = self.Kx * (Y - self.cam_height / 2)
            self.pub.publish(twi)
            print twi
        elif Y < self.top:
            twi.linear.x = self.Kx * (Y - self.cam_height / 2)
            self.pub.publish(twi)
            print twi



    def keyboard_control(self):
        command = ''
        while command != 'c':
            try:
                command = raw_input('next command : ')
                if command == 'r':
                    self.read_capture()
                else:
                    print("Invalid Command!")
            except Exception as e:
                print e


if __name__ == '__main__':
    cam=camshift_follow()
