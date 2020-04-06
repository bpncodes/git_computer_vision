import cv2
 
pt1 = (0,0)
pt2 = (0,0)
leftclick,rightclick  = False, False

def callback(event,x,y,args,flags):
    
    global pt1,pt2,leftclick,rightclick
    
    if event == cv2.EVENT_LBUTTONDOWN:
        
        if leftclick and rightclick:
            leftclick = False
            rightclick = False
            pt1 = (0,0)
            pt2 = (0,0)
            
        if not leftclick  :
            pt1= (x,y)
            leftclick = True

        elif not rightclick:
            pt2 = (x,y)
            rightclick = True

            
        

camera = cv2.VideoCapture(0)

cv2.namedWindow('frame')
cv2.setMouseCallback('frame',callback)

while True:
    
    ret,frame = camera.read()
    
    if leftclick:
        cv2.circle(frame,pt1,4,(0,255,0),-1)
    if leftclick and rightclick:
        cv2.rectangle(frame, pt1, pt2, (0,0,255), 10)
    
    
    cv2.imshow('frame', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cv2.destroyAllWindows()
camera.release()


