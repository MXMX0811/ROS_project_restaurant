#!/usr/bin/env python
import rospy
import cv2
import dlib
from std_msgs.msg import String

rospy.init_node("face_track")
cap = cv2.VideoCapture(0)
detector = dlib.get_frontal_face_detector()

last_x = 320
last_y = 240


while not rospy.is_shutdown():
	ret, frame = cap.read()
	dets = detector(frame, 1)
	left = 0
	right = 0
	top = 0
	bottom = 0
	diff = 10000
	for index, face in enumerate(dets):
		current_x = (face.left() + face.right()) / 2
		current_y = (face.top() + face.bottom()) / 2
		if abs(current_x - last_x) + abs(current_y - last_y) < diff:
			diff = abs(current_x - last_x) + abs(current_y - last_y)
			temp_x = current_x
			temp_y = current_y
			left = face.left()
			top = face.top()
			right = face.right()
			bottom = face.bottom()

	last_x = temp_x
	last_y = temp_y
	print(last_x, last_y, diff)
	cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 3)
	cv2.imshow('face',frame)
    	if cv2.waitKey(1) & 0xFF == ord('q'):
			break
	



cap.release()
cv2.destroyAllWindows()