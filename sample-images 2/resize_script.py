import cv2
import os
F=[]
for root,dirs,files in os.walk("."):
	for x in files:
		F.append(x)
for i in F:
	if i!= "resize_script.py":
		img=cv2.imread(i,0)
		img_resize=cv2.resize(img,(100,100))
		cv2.imwrite("resized_"+str(i),img_resize)

"""
# alternate solution 

import glob

images=glob.glob("*.jpg")

for image in images:
    img=cv2.imread(image,0)
    re=cv2.resize(img,(100,100))
    cv2.imshow("Hey",re)
    cv2.waitKey(500)
    cv2.destroyAllWindows()
    cv2.imwrite("resized_"+image,re) """
