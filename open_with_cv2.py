#Open images with open cv and resizing

import cv2

image = cv2.imread('DATA/00-puppy.jpg')

resized_image = cv2.resize(image,(0,0),image,0.5,0.5)

while True:
    cv2.imshow('Puppy', resized_image)
    if cv2.waitKey(0) & 0xFF == 27:
        break