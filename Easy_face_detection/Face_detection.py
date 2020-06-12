# Codigo Deteccion Facil by @doctor_python
import cv2

img_input  = cv2.imread('imagen_test.jpg')
gray_input = cv2.cvtColor(img_input, cv2.COLOR_BGR2GRAY)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
faces = face_cascade.detectMultiScale(gray_input, scaleFactor = 1.1, minNeighbors = 5)

for (x,y,w,h) in faces:
    img = cv2.rectangle(img_input,(x,y),(x+w,y+h),(0,255,255),3)
    roi_color = img[y:y+h, x:x+w]

cv2.imshow('Resultado de la deteccion',img)
cv2.waitKey(0)
cv2.destroyAllWindows()