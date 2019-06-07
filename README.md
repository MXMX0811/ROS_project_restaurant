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

First, `main.py` will wait for message from node `body_pose`. If the customer's waving is detected, the robot will say "Yes, I'm coming". If there's nobody in the visual field, the robot will turn itself to find people who is waving. And then `main.py` will publish a message to `find_people` to start the process of finding people. This process has some pause because of the delay of the Baidu API. So the robot may not drive smoothly.

When the robot is close to the customer, the robot will save its location and publish it to the topic `start_pos`. The robot will ask the customer "Hello! What would you like to have? Coffee or tea?" And then if "coffee" or "tea" is in the customer's answer, the robot will say "Yes, I'll bring you a cup of coffee/tea".

When the robot get which drink to bring, the navigation will start. Robot will drive to the fixed location and then use Kinect and `darknet_ros` to get the information (kind and depth) of the thing to catch. When the adjustment is finished, the arm will start to catch. Then the robot will drive to the customer back and say "'Here is your coffee/tea. Enjoy yourself" and raise up the drink to the customer.

## Voice interaction
Robot can publish the text to the `soundplay_node` to speak out the content.

    def talk(text):
        pub = rospy.Publisher('speech', String, queue_size=10)
        time.sleep(0.1)
        #rospy.loginfo(text)
        pub.publish(text) 
        
`text2speech.py` subscribes the topic `speech`. In the subscriber's callback function:

    def callback(data):
        pub = rospy.Publisher('speak_finish', String, queue_size=10)
        rospy.loginfo(data.data)
        soundhandle = SoundClient()
        rospy.sleep(1)
        text = data.data
        voice = 'voice_kal_diphone'
        volume = 1.0
        print 'Saying: %s' % text
        print 'Voice: %s' % voice
        print 'Volume: %s' % volume
        soundhandle.say(text, voice, volume)
        rospy.sleep(7)
        pub.publish('finish')
        
Use `xfei_asr` package to recognize the content of customer's answer. You should edit the `.cpp` before your using. You should change the sign up an account on the platform of xunfei and download the SDK. You should put the `libmsc.so` into `/catkin_ws/src/xfei_asr/lib`. And then subcribe the topic `xfwords`, and then can get the string of the words. You can write a subcriber like this:

    def listener_callback(data):
        global feed_back
        #rospy.loginfo(data.data)
        feed_back = data.data


    def listener():
        rospy.Subscriber('xfwords', String, listener_callback)
        
## Detection of the Body Key Point
The file format that Baidu API requests is Binary File. So the screen captured by the OpenCV must be transformed into binary file.

    ret, frame = cap.read()
            img_encode = cv2.imencode('.jpg', frame)[1]
            image = base64.b64encode(img_encode)
            image64 = str(image)
            image_type = "BASE64"
            params = {'image': image64,'image_type':"BASE64"}
            params = urlencode(params).encode("utf-8")
            
You may [sign up an account](http://ai.baidu.com/?track=cp:aipinzhuan|pf:pc|pp:AIpingtai|pu:title|ci:|kw:10005792) and then get `access_token` by this way:

    curl -i -k 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=（This is API Key）&client_secret=（This is Secret Key）'
   
The access_token should be updated by month.

    request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/body_analysis"
    access_token = '[24.cb4ed767145d6bc628ca085d6ea3f3d3.2592000.1561474761.282335-16350696]'
    request_url = request_url + "?access_token=" + access_token
    request = urllib2.urlopen(url=request_url, data=params)
    
It may spend about 1s to get the result. The returned information's form is similar to `json`. You can use this method to change it into json:

    content = request.read()  
    result = str(content)
    res = json.loads(result)
    
In `res['person_num']` is the number of the people, and each person's information is in `res['person_info']`. You can get the first person's key points postions in `res['person_info'][0]['body_parts']`. You can use OpenCV draw some points and lines to mark the positions on the screen.


![](https://github.com/nkMengXin/ROS_project_restaurant/raw/master/body_pose.png)

Get the average of the postion of hip and neck as the y_error and x_error.

    body_height = ((jo.dic['right_hip']['y'] + jo.dic['left_hip']['y']) / 2 + jo.dic['neck']['y']) / 2
    pub_height.publish(str(body_height))

    body_error = (((jo.dic['right_hip']['x'] + jo.dic['left_hip']['x']) / 2) + jo.dic['neck']['x']) / 2
    pub_x_error.publish(str(body_error))

`find_people` will use these error to drive to customer.


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
