import numpy as np
import cv2

face_cascade = cv.CascadeClassifier ( 'haarcascade_frontalface_default.xml' )
eye_cascade = cv.CascadeClassifier ( 'haarcascade_eye.xml' )
img = cv.imread ( 'img_face.png' )
gris = cv.cvtColor (img, cv.COLOR_BGR2GRAY)

faces = faces_cascade.detectMultiScale(gris, 1.3,5 )

for (x, y, w, h) in faces:
    cv.rectangle (img, (x, y), (x + w, y + h), (255,0,0), 2)
    roi_gray = gris [y: y + h, x: x + w]
    roi_color = img [y: y + h, x: x + w]
    eyes = eye_cascade.detectMultiScale (roi_gray)
    for (ex, ey, ew, eh) in ojos:
        cv.rectangle (roi_color, (ex, ey), (ex + ew, ey + eh), (0,255,0), 2)
        
cv.imshow( 'img' , img)
cv.waitKey(0)
cv.destroyAllWindows()
