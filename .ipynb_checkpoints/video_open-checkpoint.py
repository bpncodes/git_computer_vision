import cv2

cap = cv2.VideoCapture(0)

def called(event, x, y, flags, args):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.rectangle(frame, (x, y),( x+100, y+100), (0,0,255), 10,10)
    

cv2.namedWindow('frame')
cv2.setMouseCallback('frame', called)


while True:
    
    ret, frame = cap.read()
    
    cv2.imshow('frame', frame)
    
    if cv2.waitKey(0) & 0xFF == ord('q') :
        break
        

cap.release()
cv2.destroyAllWindows()