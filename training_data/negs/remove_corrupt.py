from PIL import Image
import os

for file in os.listdir("./neg_img"):
	try:
		img=Image.open("./neg_img/"+file)
		img.verify()

	except(IOError,SyntaxError) as e:
		print "removing",file
		os.remove("./neg_img/"+file)