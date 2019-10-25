import cv2
import numpy

def run_process():
	for i in range(1,76):
		try:
			img_gray=cv2.imread("fist/img/"+"fist_test"+str(i)+".jpg",cv2.IMREAD_GRAYSCALE)
			resiz=cv2.resize(img_gray,(100,100))
			cv2.imwrite("fist/img/"+"fist_test"+str(i)+".jpg",resiz)
		except Exception as e:
			print("failed -",e)


run_process()
