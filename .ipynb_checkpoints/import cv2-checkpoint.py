import cv2

img = cv2.imread('DATA/00-puppy.jpg')


while True:

    img = cv2.resize(img, (20,20))
    cv2.imshow('img',img)

    if cv2.waitKey(1) & 0xFF == 27:
        break