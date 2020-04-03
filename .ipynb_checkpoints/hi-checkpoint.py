import cv2

imread = cv2.imread('DATA/00-puppy.jpg')

while True:
    cv2.resize(imread, (300,300))
    cv2.imshow('bipin', imread)
    if cv2.waitKey(0) & 0xFF == 27:
        break


# if cv2.waitKey(0) and 0xFF (Also in binary 11111111 that is only the 8 bit
# that is the key pressed) if equals to 27 ie ord(esc key ) then we return
