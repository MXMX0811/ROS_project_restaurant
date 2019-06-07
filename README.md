# ROS_project_restaurant
## Overview
This is a `ROS` project developed on the basis of `RoboCup@Home` `Restaurant`. The project is running on the turtlebot2 with a robotic arm and Kinect. The robot can find the customer who is waving to the robot and then drive to the customer and ask what kind of drink does the customer want. And then the robot can drive to the location fixed on the map previously and recognize which kind of drink to catch. Finally the robot can bring the drink back to the customer.

__Auther: [Zhang Mingxin](https://github.com/nkMengXin), 1611260__

![](https://github.com/nkMengXin/ROS_project_restaurant/raw/master/A2EEFCC228E3F8F6F3BA90471DA6E8BF.png)

* Based on the [Baidu API](https://cloud.baidu.com/product/body), can recognize the key points of human body(like wrists, nose and neck).

* Based on the [darknet_ros](https://github.com/leggedrobotics/darknet_ros) package, can achieve the Real-Time Object Detection.

* The tuetlebot's navigation is based on the package `rchomeedu_navigation`.

* The robotic arm's catching is based on the package `rchomeedu_arm`.

* The voice interaction is based on `xfei_asr`.

## Navigation
In the file catkin_ws/src/rc-home-edu-learn-ros/rchomeedu_navigation/scripts/my_navigation.py is the process of the navigation between the fixed location and the customer's location which received from the node `find_people`.

    def get_start_pose(self, start_pose):
      global A_x, A_y, A_theta
      pose = start_pose.data.split(',')
      A_x = float(pose[0])
      A_y = float(pose[1])
      A_theta = float(pose[2])

The `function get_start_pose` will be called when this is executing:

    rospy.Subscriber('start_pos', String, self.get_start_pose)
