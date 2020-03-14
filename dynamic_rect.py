# Imports 
import numpy as np
import cv2

# Variables
ix, iy = -1, -1 
draw = False

# Callback Functions
def callBackFunction(event, x, y, flags, args):
        global ix, iy, draw
        if event == cv2.EVENT_LBUTTONDOWN:
            draw = True
            ix, iy = x, y
        elif event == cv2.EVENT_MOUSEMOVE:
            if draw:
                cv2.rectangle(img, (ix, iy), (x, y), (0,255,0),-1 )
        elif event == cv2.EVENT_LBUTTONUP:
            draw = False
            cv2.rectangle(img, (ix, iy), (x, y), (0,255,0), -1)

# Listeners



temp_img = cv2.imread('DATA/pup.jpg')

img = cv2.resize(temp_img, (0,0), temp_img, 0.5, 0.5)

cv2.namedWindow(winname = 'puppy')

cv2.setMouseCallback('puppy', callBackFunction)


# Image init
while 1:
    
    cv2.imshow('puppy', img)
    
    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()