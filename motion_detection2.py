import cv2, time
import pandas
from datetime import datetime
first_frame=None

status_list=[None,None]

times=[]

df=pandas.DataFrame(columns=["start","end"])
video=cv2.VideoCapture(0)
while True:
	
	check,frame=video.read()
	# print(check)
	status=0
	# print(frame)

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
		status=1	
		(x,y,w,h)=cv2.boundingRect(contour)
		cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,12),3)


	status_list.append(status)
	status_list=status_list[-2:]

	if status_list[-1]==1 and status_list[-2]==0:
		times.append(datetime.now())
	if status_list[-1]==0 and status_list[-2]==1:
		times.append(datetime.now())
	cv2.imshow("Capturing",gray)
	cv2.imshow("delta",delta_frame)
	cv2.imshow("thresh_delta",thresh_frame)
	cv2.imshow("rectangle",frame)
	key=cv2.waitKey(1)

	# print(gray)
	# print(status)


	if key==ord('q'):
		if status==1:
			times.append(datetime.now()) #this if for when obj is in screen and we quit
		break

print(status_list)
print(times)

for i in range(0,len(times),2):
	df=df.append({"start":times[i],"end":times[i+1]},ignore_index=True)

df.to_csv("times.csv")
video.release()
cv2.destroyAllWindows()
