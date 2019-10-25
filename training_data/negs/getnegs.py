import urllib
import time

file=open("neg_urls.txt")

count=0
for url in file.readlines():
	try:
		print "importing image",count
		urllib.urlretrieve(url,"neg_img/neg_"+str(count)+".jpg")
		count+=1
	except Exception as e:
		print e
		continue


