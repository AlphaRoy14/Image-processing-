import cv2

img=cv2.imread("galaxy.jpg",0)

print(type(img))
print(img.shape)
print(img.ndim) #image dimention


resized_image=cv2.resize(img,(580,800))
resized_image=cv2.resize(img,(int(img.shape[1]/2),int(img.shape[0]/2)))

cv2.imwrite("galazt_resized.jpg",resized_image) #to write it in a file
cv2.imshow("Galaxy",resized_image) #opens a window 
cv2.waitKey(10000) #to freeze the screen for 10 secs
cv2.destroyAllWindows() #kills the scrren if theres an interupt from input
