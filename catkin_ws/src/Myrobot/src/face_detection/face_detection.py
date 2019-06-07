#!/usr/bin/env python
import rospy
import cv2
import dlib
from std_msgs.msg import String

rospy.init_node("find_face")
pub = rospy.Publisher('find_face', String, queue_size=10)
cap = cv2.VideoCapture(0)
detector = dlib.get_frontal_face_detector()

while not rospy.is_shutdown():
	ret, frame = cap.read()
	dets = detector(frame, 1)
	print("Number of faces detected: {}".format(len(dets)))
	for index, face in enumerate(dets):
		print('face {}; left {}; top {}; right {}; bottom {}'.format(index,
                                                                     face.left(), face.top(), face.right(),
                                                                     face.bottom()))
		left = face.left()
		top = face.top()
		right = face.right()
		bottom = face.bottom()
		cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 3)
	cv2.imshow('face',frame)
    	if cv2.waitKey(1) & 0xFF == ord('p'):
			pub.publish("Number of faces detected:" + format(len(dets)))
	



cap.release()
cv2.destroyAllWindows()


