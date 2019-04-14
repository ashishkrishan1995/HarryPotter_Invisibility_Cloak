import cv2
import numpy as np
import time

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))

cap = cv2.VideoCapture(0)
time.sleep(3)
background=0
for i in range(30):
	ret,background = cap.read()

background = np.flip(background,axis=1)

while(cap.isOpened()):
	ret, img = cap.read()
        
	img = np.flip(img,axis=1)
	hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

	# Generating mask to detect red color
	lower_red = np.array([0,100,100])
	upper_red = np.array([10,255,255])
	mask1 = cv2.inRange(hsv,lower_red,upper_red)

	lower_red = np.array([160,100,100])
	upper_red = np.array([180,255,255])
	mask2 = cv2.inRange(hsv,lower_red,upper_red)

	mask = mask1 + mask2
	mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((3,3),np.uint8))
	
	img[np.where(mask==255)] = background[np.where(mask==255)]
	out.write(img)
	
	cv2.imshow('Invisibility Cloak',img)
	k = cv2.waitKey(10)
	if k == 27:
		break

