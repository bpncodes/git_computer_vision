import cv2
import matplotlib.pyplot as plt

def callback(event, x, y, args, flags):
    if event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(img, (x,y), 20, (0,0,255), 10)

cv2.namedWindow('back')
cv2.setMouseCallback('back', callback)

img = cv2.imread('DATA/dog_backpack.jpg')
img = cv2.resize(img, (0,0), img, 0.5, 0.5)

while True:
    cv2.imshow('back', img)
    if cv2.waitKey(1) & 0xFF == 27:
        break