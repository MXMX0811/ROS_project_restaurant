#!/usr/bin/env python
# encoding: utf-8
import rospy
import os
import cv2
import dlib
from std_msgs.msg import String
from geometry_msgs.msg import Twist
import base64
import urllib2
import sys,base64
import json
from urllib import urlencode
import time
import math

class Joint(object):
     
    __circle_list = []
     
    def __init__(self,dic):   
        self.dic = dic
     
    def draw_line(self,img):
        #nose ---> neck
        if int(self.dic['nose']['x']) and int(self.dic['nose']['y']) and int(self.dic['neck']['x']) and int(self.dic['neck']['y']):
            cv2.line(img, (int(self.dic['nose']['x']),int(self.dic['nose']['y'])),
					(int(self.dic['neck']['x']),int(self.dic['neck']['y'])), (0,0,255), 2)
        #neck --> left_shoulder
        if int(self.dic['neck']['x']) and int(self.dic['neck']['y']) and int(self.dic['left_shoulder']['x']) and int(self.dic['left_shoulder']['y']):
            cv2.line(img, (int(self.dic['neck']['x']),int(self.dic['neck']['y'])),
					(int(self.dic['left_shoulder']['x']),int(self.dic['left_shoulder']['y'])), (0,0,255), 2)       
        #neck --> right_shoulder
        if int(self.dic['neck']['x']) and int(self.dic['neck']['y']) and int(self.dic['right_shoulder']['x']) and int(self.dic['right_shoulder']['y']):
            cv2.line(img, (int(self.dic['neck']['x']),int(self.dic['neck']['y'])),
					(int(self.dic['right_shoulder']['x']),int(self.dic['right_shoulder']['y'])), (0,0,255), 2)       
        #left_shoulder --> left_elbow
        if int(self.dic['left_shoulder']['x']) and int(self.dic['left_shoulder']['y']) and int(self.dic['left_elbow']['x']) and int(self.dic['left_elbow']['y']):
            cv2.line(img, (int(self.dic['left_shoulder']['x']),int(self.dic['left_shoulder']['y'])),
					(int(self.dic['left_elbow']['x']),int(self.dic['left_elbow']['y'])), (0,0,255), 2)        
        #left_elbow --> left_wrist
        if int(self.dic['left_elbow']['x']) and int(self.dic['left_elbow']['y']) and int(self.dic['left_wrist']['x']) and int(self.dic['left_wrist']['y']):
            cv2.line(img, (int(self.dic['left_elbow']['x']),int(self.dic['left_elbow']['y'])),
					(int(self.dic['left_wrist']['x']),int(self.dic['left_wrist']['y'])), (0,0,255), 2)        
        #right_shoulder --> right_elbow
        if int(self.dic['right_shoulder']['x']) and int(self.dic['right_shoulder']['y']) and int(self.dic['right_elbow']['x']) and int(self.dic['right_elbow']['y']):
            cv2.line(img, (int(self.dic['right_shoulder']['x']),int(self.dic['right_shoulder']['y'])),
					(int(self.dic['right_elbow']['x']),int(self.dic['right_elbow']['y'])), (0,0,255), 2)         
        #right_elbow --> right_wrist
        if int(self.dic['right_elbow']['x']) and int(self.dic['right_elbow']['y']) and int(self.dic['right_wrist']['x']) and int(self.dic['right_wrist']['y']):
            cv2.line(img, (int(self.dic['right_elbow']['x']),int(self.dic['right_elbow']['y'])),
					(int(self.dic['right_wrist']['x']),int(self.dic['right_wrist']['y'])), (0,0,255), 2)        
        #neck --> left_hip
        if int(self.dic['neck']['x']) and int(self.dic['neck']['y']) and int(self.dic['left_hip']['x']) and int(self.dic['left_hip']['y']):
            cv2.line(img, (int(self.dic['neck']['x']),int(self.dic['neck']['y'])),
					(int(self.dic['left_hip']['x']),int(self.dic['left_hip']['y'])), (0,0,255), 2)        
        #neck --> right_hip
        if int(self.dic['neck']['x']) and int(self.dic['neck']['y']) and int(self.dic['right_hip']['x']) and int(self.dic['right_hip']['y']):
            cv2.line(img, (int(self.dic['neck']['x']),int(self.dic['neck']['y'])),
					(int(self.dic['right_hip']['x']),int(self.dic['right_hip']['y'])), (0,0,255), 2)      
        #left_hip --> left_knee
        if int(self.dic['left_hip']['x']) and int(self.dic['left_hip']['y']) and int(self.dic['left_knee']['x']) and int(self.dic['left_knee']['y']):
            cv2.line(img, (int(self.dic['left_hip']['x']),int(self.dic['left_hip']['y'])),
					(int(self.dic['left_knee']['x']),int(self.dic['left_knee']['y'])), (0,0,255), 2)       
        #right_hip --> right_knee
        if int(self.dic['right_hip']['x']) and int(self.dic['right_hip']['y']) and int(self.dic['right_knee']['x']) and int(self.dic['right_knee']['y']):
            cv2.line(img, (int(self.dic['right_hip']['x']),int(self.dic['right_hip']['y'])),
					(int(self.dic['right_knee']['x']),int(self.dic['right_knee']['y'])), (0,0,255), 2)       
        #left_knee --> left_ankle
        if int(self.dic['left_knee']['x']) and int(self.dic['left_knee']['y']) and int(self.dic['left_ankle']['x']) and int(self.dic['left_ankle']['y']):
            cv2.line(img, (int(self.dic['left_knee']['x']),int(self.dic['left_knee']['y'])),
					(int(self.dic['left_ankle']['x']),int(self.dic['left_ankle']['y'])), (0,0,255), 2)       
		#right_knee --> right_ankle
        if int(self.dic['right_knee']['x']) and int(self.dic['right_knee']['y']) and int(self.dic['right_ankle']['x']) and int(self.dic['right_ankle']['y']):
            cv2.line(img, (int(self.dic['right_knee']['x']),int(self.dic['right_knee']['y'])),
					(int(self.dic['right_ankle']['x']),int(self.dic['right_ankle']['y'])), (0,0,255), 2)
         
    def xunhun(self,img):
        #im1 = cv2.imread(img,cv2.IMREAD_COLOR)
        im1 = img
         
        for i in self.dic:
            if int(self.dic[i]['x']) and int(self.dic[i]['y']):
                cv2.circle(im1,(int(self.dic[i]['x']),int(self.dic[i]['y'])),5,(0,0,255),-1)
                
        self.draw_line(im1)
        cv2.imshow('image',im1)

if __name__ == '__main__':
    if_find = 0
    rospy.init_node("body_pose")
    pub_hello = rospy.Publisher('hello', String, queue_size=10) #是否招手
    pub_height = rospy.Publisher('body_height', String, queue_size=10)  #身体高度（用于确定距离）
    pub_x_error = rospy.Publisher('body_x_error', String, queue_size=10)    #用于确定位置
    pub = rospy.Publisher('/cmd_vel_mux/input/navi', Twist, queue_size=5)

    cap = cv2.VideoCapture(0)


    while not rospy.is_shutdown():
        
        ret, frame = cap.read()

        img_encode = cv2.imencode('.jpg', frame)[1]

        request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/body_analysis"
        image = base64.b64encode(img_encode)
        image64 = str(image)
        image_type = "BASE64"
        
        params = {'image': image64,'image_type':"BASE64"}
        
        params = urlencode(params).encode("utf-8")
        #access_token需要每30天更新
        #通过以下命令获取
        #curl -i -k 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=（此处为API Key）&client_secret=（此处为Secret Key）'
        access_token = '[24.cb4ed767145d6bc628ca085d6ea3f3d3.2592000.1561474761.282335-16350696]'
        request_url = request_url + "?access_token=" + access_token

        #响应时间约为1s
        time_start=time.time()
        request = urllib2.urlopen(url=request_url, data=params)
        time_end=time.time()

        content = request.read()  
        result = str(content)
        res = json.loads(result)
        print(res)
    
        if ('person_info' in res) and res['person_info']!='':
            ress = res['person_info'][0]['body_parts']
            jo = Joint(ress)
            jo.xunhun(frame)

        else:
            twi = Twist()
            twi.angular.z = 0.1
            pub.publish(twi)

        dist_hand_face = math.sqrt((jo.dic['right_wrist']['y'] - jo.dic['nose']['y'])**2 + (jo.dic['right_wrist']['x'] - jo.dic['nose']['x'])**2)
        dist_shoulder = math.sqrt((jo.dic['right_shoulder']['y'] - jo.dic['left_shoulder']['y'])**2 + (jo.dic['right_shoulder']['x'] - jo.dic['left_shoulder']['x'])**2)
        
        if if_find == 0 and  dist_hand_face < 1.2*dist_shoulder and jo.dic['right_wrist']['y']:
            #若手在脸部周围则为招手(1.2倍肩宽)
            pub_hello.publish('yes!')
            print('yes!')
            if_find = 1

        elif jo.dic['right_wrist']['y'] == 0 or jo.dic['right_shoulder']['y'] == 0:
            if_find = 0
            print('失去目标，重置')

        if jo.dic['right_hip']['y'] and jo.dic['left_hip']['y'] and jo.dic['neck']['y']:
            #body_height = (jo.dic['right_hip']['y'] + jo.dic['left_hip']['y']) / 2 - jo.dic['neck']['y']
            body_height = ((jo.dic['right_hip']['y'] + jo.dic['left_hip']['y']) / 2 + jo.dic['neck']['y']) / 2
            pub_height.publish(str(body_height))
            print('body_height', body_height)

        if jo.dic['right_hip']['x'] and jo.dic['left_hip']['x'] and jo.dic['neck']['x']:
            #body_error = 320 - (((jo.dic['right_hip']['x'] + jo.dic['left_hip']['x']) / 2) + jo.dic['neck']['x']) / 2
            body_error = (((jo.dic['right_hip']['x'] + jo.dic['left_hip']['x']) / 2) + jo.dic['neck']['x']) / 2
            pub_x_error.publish(str(body_error))
            print('body_error', body_error)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        



    cap.release()
    cv2.destroyAllWindows()