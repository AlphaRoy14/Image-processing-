import cv2

face_cascader=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
img=cv2.imread("photo2.jpg")
gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

face=face_cascader.detectMultiScale(gray_image,
scaleFactor=1.15,minNeighbors=12)

for x,y,w,h in face:
	img=cv2.rectangle(img,(x,y),(x+w,y+h),(0,244,5),12)
resized_image=cv2.resize(img,(int(img.shape[1]/5),int(img.shape[0]/5)))
cv2.imshow("Photo",resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()