#!/usr/bin/env python
# encoding: utf-8


import rospy
import time
from std_msgs.msg import String
from geometry_msgs.msg import PoseWithCovarianceStamped


def listener_callback(data):
	global feed_back
	#rospy.loginfo(data.data)
	feed_back = data.data
	
	
def listener():
    rospy.Subscriber('xfwords', String, listener_callback)

def hello():
    rospy.Subscriber('hello', String, hello_callback)

def hello_callback(data):
	global is_start
	if data.data == 'yes!':
		is_start = 1


def talk(text):
    pub = rospy.Publisher('speech', String, queue_size=10)
    time.sleep(0.1)
    #rospy.loginfo(text)
    pub.publish(text)   
  

if __name__ == '__main__':
	rospy.init_node('main', anonymous=True)
	rospy.wait_for_message('initialpose', PoseWithCovarianceStamped)	#等待设定初始位姿
	pub_navi_start = rospy.Publisher('start_navi', String, queue_size=10)
	pub_find_start = rospy.Publisher('start_find', String, queue_size=10)
	is_start = 0
	while not rospy.is_shutdown():
		hello()
		rospy.wait_for_message('hello', String)
		if is_start == 1:
			print("Yes! I'm coming.")
			talk("Yes! I'm coming.")
			rospy.wait_for_message('speak_finish', String)
			break

	time.sleep(2)
	pub_find_start.publish('finding_start')	#发布消息，走到目标人附近
	rospy.wait_for_message('finding_finish', String)	#已经走到目标人附近

	talk("Hello! What would you like to have? Coffee or tea?")
	feed_back = '0'
	rospy.wait_for_message('speak_finish', String)
	print("talking finished")
	time.sleep(3)
	while not rospy.is_shutdown():
		listener()
		if feed_back!='0':
			print('success!')
			print(feed_back)
			if '咖啡' in feed_back or 'coffee' in feed_back:
				print('coffee')
				drink = 'coffee'
				talk("OK. I'll bring you a cup of coffee")
				#talk("好的，我去给您拿一杯咖啡")
				rospy.wait_for_message('speak_finish', String)
				break
			elif '茶' in feed_back or 'tea' in feed_back:
				print('tea')
				drink = 'tea'
				talk("OK. I'll bring you a cup of tea")
				#talk("好的，我去给您拿一杯茶")
				rospy.wait_for_message('speak_finish', String)
				break
			else:
				talk("I'm not sure I understand.")
				#talk("我不明白你的意思")
				rospy.wait_for_message('speak_finish', String)

	print('finish!')
	pub_navi_start.publish('start_navi')
	rospy.wait_for_message('navi_finish', String)
	print('finish navi')
	talk('Here is your' + drink + '. Enjoy yourself.')
	rospy.wait_for_message('speak_finish', String)
	time.sleep(200)	#此处为导航过程
