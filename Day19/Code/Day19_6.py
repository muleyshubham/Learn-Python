#draw shapes using cv2

import cv2
import numpy as np

#create empty image(canvas)
canvas = np.ones((400,400,3),dtype=np.uint8)

#change canvas color to white
#canvas = canvas * 255
#line,rectange,arc,circle,arrow,text
cv2.rectangle(canvas,(100,100),(350,200),(0,0,255),cv2.LINE_4)
cv2.circle(canvas,(300,300),50,(255,0,0),cv2.LINE_4)


#show the image
cv2.imshow('CANVAS',canvas)

#waitKey function
cv2.waitKey(0)

# destroy all the windows
cv2.destroyAllWindows()
