import numpy as np
import cv2
from matplotlib import pyplot as plt

###########################################################
def checkpoints(img):
	#pointsInLine = [(250,450),(250,350),(390,450),(390,350)]
	
	leftPath=rightPath=True
	while True:
		for i in range(350,450):
			pixval = int(img[i,220])
			leftPath = True
			if pixval==255:
				leftPath = False
				break
			
				
		for i in range(350,450):
			pixval = int(img[i,420])
			rightPath = True
			if pixval==255:
				rightPath = False
				break
				
		return (leftPath,rightPath)
		
############################################################

def GuidePath(imag) :
	#img = cv2.imread(path)#'Testimages/2019-03-09-092512.jpg')
	#imag = cv2.imread(imag_path)
	img = imag
	"""cv2.imshow("image",img)
	cv2.waitKey(900)
	cv2.destroyAllWindows()"""
	gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	ret, thresh = cv2.threshold(gray,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)


	# noise removal
	kernel = np.ones((3,3),np.uint8)
	opening = cv2.morphologyEx(thresh,cv2.MORPH_OPEN,kernel, iterations = 2)

	# sure background area
	sure_bg = cv2.dilate(opening,kernel,iterations=3)

	# Finding sure foreground area
	dist_transform = cv2.distanceTransform(opening,cv2.DIST_L2,5)
	ret, sure_fg = cv2.threshold(dist_transform,0.7*dist_transform.max(),255,0)

	# Finding unknown region
	sure_fg = np.uint8(sure_fg)
	unknown = cv2.subtract(sure_bg,sure_fg)

	pixval = int(unknown[400,320])   #Coordinates are input oppositely than line drawing -- image[height][width]
	print(pixval)

	if pixval==255:
		(left,right) = checkpoints(unknown)
		if left==True:
			print("Strafe left and move forward")
			return "Strafe left and move forward"
		elif right==True:
			print("Strafe right and move forward")
			return "Strafe right and move forward"
		else:
			print("No path further.. Aborted")
			return "No path further.. Aborted"
	else:
		print("Move forward")
		return "Move forward"	

	# Printing out the crosshair
	img = cv2.cvtColor(unknown,cv2.COLOR_GRAY2BGR)
	img = cv2.line(img,(320,400),(320,400),(0,255,0),5)
	img = cv2.line(img,(220,350),(220,450),(0,255,0),5)
	img = cv2.line(img,(420,350),(420,450),(0,255,0),5)


	"""cv2.imshow("image",img)
	cv2.waitKey(900)
	cv2.destroyAllWindows()"""
	#img = cv2.line(img,(0,480),(320,360),(0,255,0),3)   #Comment out... Only for debug purpose
	#img = cv2.line(img,(320,360),(640,480),(0,255,0),3) #Same as previous line  ## Syntax: cv2.line(...(width,height)...)

	#cv2.imwrite("cont.jpg",img)



		
				
		
