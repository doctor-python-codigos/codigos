import cv2

cap = cv2.VideoCapture(0)

while(True):
    
    ret, frame = cap.read()
    frame = cv2.resize(frame, None, fx=1.0, fy=1.0)
    cv2.imshow("Doctor Python Tutorial", frame)
    c = cv2.waitKey(1)
    
    # presionar esc para cerrar la ventana
    if c == 27:
    	break 

cap.release()
cv2.destroyAllWindows()