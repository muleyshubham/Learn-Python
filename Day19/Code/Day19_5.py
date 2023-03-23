# convert the color image to gray scale
import cv2
import numpy as np

# read the image
img=cv2.imread("./messi5.jpg")

#convert the color image to gray scale
gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

cv2.imshow("Original ",img)
cv2.imshow("Gray Scale ",gray_img)

cv2.waitKey(0)

cv2.destroyAllWindows()
