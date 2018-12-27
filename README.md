# Detección de Rostros con Python y OpenCV

La Detección de objetos usando los clasificadores en cascada basados en características de Haar es un método efectivo de detección de objetos propuesto por Paul Viola y Michael Jones en su artículo, "Detección rápida de objetos usando una cascada aumentada de características simples" en 2001. Es un enfoque basado en el aprendizaje automático donde La función de cascada se entrena a partir de muchas imágenes positivas y negativas. Luego se utiliza para detectar objetos en otras imágenes.

Primero necesitamos cargar los clasificadores XML requeridos. Luego cargar nuestra imagen de entrada (o video) en modo de escala de grises.

```python
import numpy as np
import cv2

face_cascade = cv.CascadeClassifier ( 'haarcascade_frontalface_default.xml' )
eye_cascade = cv.CascadeClassifier ( 'haarcascade_eye.xml' )
img = cv.imread ( 'img_face.png' )
gris = cv.cvtColor (img, cv.COLOR_BGR2GRAY)

```

```
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
```



!["https://github.com/LuisAlejandroSalcedo/Deteccion-de-Rostros-con-Python/Resultado.png"]

