import cv2, time
first_frame=None
video=cv2.VideoCapture(0)
while True:
	
	check,frame=video.read()
	print(check)
	print(frame)

	gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	gray=cv2.GaussianBlur(gray,(21,21),0) #we are blurring the image to reducd the noice and more accuracy
	if first_frame is None:
		first_frame=gray
		continue

	delta_frame=cv2.absdiff(first_frame,gray)
	thresh_frame=cv2.threshold(delta_frame,30,255,cv2.THRESH_BINARY)[1] #dead the doc --> it'll return a tupple we need to access the 2nd element
	# the above code will take a threshhold limit, for this case 30, so any element 
	# in the matrix having a value greater than 30 will be made color 255 and cv2.THRESH_BINARY is a method (many more available you can choose)
	thresh_frame=cv2.dilate(thresh_frame,None,iterations=1) #dilate to removet the holes in the b&w image , None is for kernal matrix

	(_,cnts,_)=cv2.findContours(thresh_frame.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)  #to retrieve approximate ecternal countours 
	# ^weird syntx

	for contour in cnts:
		if cv2.contourArea(contour) < 1000:
			continue
		(x,y,w,h)=cv2.boundingRect(contour)
		cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,12),3)



	cv2.imshow("Capturing",gray)
	cv2.imshow("delta",delta_frame)
	cv2.imshow("thresh_delta",thresh_frame)
	cv2.imshow("rectangle",frame)
	key=cv2.waitKey(1)

	print(gray)

	if key==ord('q'):
		break
print(a)
video.release()
cv2.destroyAllWindows()