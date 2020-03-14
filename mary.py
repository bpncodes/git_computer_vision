import cv2
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
#Variables
draw = False
ix, iy = -1, -1

#Functions
def touch(event, x, y, flags, args):
    global draw, ix, iy
    if event == cv2.EVENT_LBUTTONDOWN:
        draw = True
        ix, iy = x, y
    elif event == cv2.EVENT_MOUSEMOVE:
        if draw:
            cv2.rectangle(img,(ix,iy), (x,y), (0,0,255), -1)
    elif event == cv2.EVENT_LBUTTONUP:
        draw = False
        cv2.rectangle(img,(ix,iy), (x,y), (0,0,255), -1)

#Initialise images
img_opened = cv2.imread('DATA/pup.jpg')
img = cv2.resize(img_opened,(0,0), img_opened, 0.5, 0.5)
cv2.namedWindow('puppy')
cv2.setMouseCallback('puppy', touch)

#Open images
while True:
    cv2.imshow('puppy', img)
    if cv2.waitKey(1) & 0xFF == 27:
        break