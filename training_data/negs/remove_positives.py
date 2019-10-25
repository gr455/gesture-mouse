import cv2
import os
import time
import numpy

def delPos():
	cascade_fist=cv2.CascadeClassifier("pos_fist.xml")
	for file in os.listdir("./neg_img"):
		#print file
		img=cv2.imread("./neg_img/"+file)
		processed_img=cv2.GaussianBlur(cv2.cvtColor(img,cv2.COLOR_BGR2GRAY),(21,21),0)

		detect_fist=cascade_fist.detectMultiScale(processed_img,scaleFactor=1.05,minNeighbors=75)
		if(detect_fist!=() ):
			print "removing", file
			os.remove("./neg_img/"+file)

delPos()