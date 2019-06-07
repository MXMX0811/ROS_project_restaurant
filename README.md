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

## main.py
`main.py` is used to control and manage all of the functions of the robot. Because the ROS nodes are parallel, so we can use wait_for_message() to block the process of the programme and then publish some messages to it to let it countinue. The function is used like this:

    rospy.wait_for_message('topic name', type)

It will initiate a subscriber, and when the message is received, destroy the subscriber.

First, `main.py` will wait for message from node `body_pose`. If the customer's waving is detected, the robot will say "Yes, I'm coming.". If there's nobody in the visual field, the robot will turn itself to find people who is waving. And then `main.py` will publish a message to `find_people` to start the process of finding people. This process has some pause because of the delay of the Baidu API. So the robot may not drive smoothly.

## Navigation
In the file `catkin_ws/src/rc-home-edu-learn-ros/rchomeedu_navigation/scripts/my_navigation.py` is the process of the navigation between the fixed location and the customer's location which received from the node `find_people`.

    def get_start_pose(self, start_pose):
      global A_x, A_y, A_theta
      pose = start_pose.data.split(',')
      A_x = float(pose[0])
      A_y = float(pose[1])
      A_theta = float(pose[2])

The `function get_start_pose` will be called when this is executed:

    rospy.Subscriber('start_pos', String, self.get_start_pose)

The location of the customer will be saved as A_x, A_y and A_theta. These will be transformed into quaternion and then sent to movebase.

The robot will go to the fixed location (saved as B) when:

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
            pub.publish('ready_to_catch') 	#publish message to the node used to control the catching
            rospy.wait_for_message('arm2navi', String)	#countinue when the catching finish

And when the catching process finish, the robot will go back to A. This part of code is similar to above. And then this node will publish a message that tells the arm should raise the drink to the customer.
