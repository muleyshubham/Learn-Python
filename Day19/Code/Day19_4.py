#images
# open CV
import cv2
import numpy as np

def function1():
    #read an image
    img = cv2.imread("./messi5.jpg")
    print(img) # gives the information in the BGR Format
    # B:Blue G:Green R:RED
    print("-"*80)
    print(f"Type = {type(img)}")
    print(f"Shape = {img.shape}") # (w,h,ch)
    #w : width h : Height ch : channel
    w,h,ch = img.shape # Unpacking
    print(f"Size = {w}*{h}")
#function1()

def function2():
    # read an image
    img = cv2.imread("./messi5.jpg")

    #show the image
    cv2.imshow("MESSI",img)

    # wait for some key to be pressed
    #cv2.waitKey(5000) #image will be shown for 5 seconds
    cv2.waitKey(0)
    cv2.destroyAllWindows()

function2()