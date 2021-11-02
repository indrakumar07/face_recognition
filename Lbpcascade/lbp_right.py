import cv2
import face_recognition
cap= cv2.VideoCapture('a5.mp4')
cascadePath = "lbpcascade_profileface.xml"
faceCascade = cv2.CascadeClassifier(cascadePath)
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == False:
        break
    img = cv2.resize(frame,(640,480))
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray)
    if len(faces)>0:
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        cv2.imshow('Video', img)  
    k = cv2.waitKey(30) & 0xff  
    if k==27:  
        break   
cap.release()
cv2.destroyAllWindows()