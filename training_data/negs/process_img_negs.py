import cv2
import os

def run_process():
	try:
		for file in os.listdir('./neg_img'):
			print "resizing",file
			img=cv2.imread("./neg_img/"+file)
			img_proc=cv2.resize(img,(200,200))
			cv2.imwrite("./neg_img/"+file,img_proc)
	except Exception as e:
		print e
	


run_process()
