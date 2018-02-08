import cv2, time

a=0
video=cv2.VideoCapture(0)
while True:
	a+=1
	check,frame=video.read()
	print(check)
	print(frame)

	gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

	face_cascader=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
	faces=face_cascader.detectMultiScale(gray,scaleFactor=1.15,minNeighbors=6)

	for x,y,w,h in faces:
		frame=cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,10),12)

	#time.sleep(5)

	cv2.imshow("Capturing",frame)
	key=cv2.waitKey(1)
	if key==ord('q'):
		break
print(a)
video.release()
cv2.destroyAllWindows()