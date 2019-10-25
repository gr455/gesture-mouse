import os

dat=open("neg_list.txt",'a')
try:
	for file in os.listdir("./neg_img"):
		dat.write("neg_img/"+file+'\n')
except Exception:
	pass

