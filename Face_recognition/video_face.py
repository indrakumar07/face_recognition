import cv2
import face_recognition
cap= cv2.VideoCapture('a2.mp4')
i=0
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == False:
        break
    img = cv2.resize(frame,(640,480))
    res=face_recognition.face_locations(img)
    for i in res:
        x,y,w,h=i
        cv2.rectangle(img, (h, x), (y, w), (0, 0, 255), 2)
    cv2.imshow('Video', img)  
    k = cv2.waitKey(30) & 0xff  
    if k==27:  
        break   
cap.release()
cv2.destroyAllWindows()
