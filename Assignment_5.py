import cv2
import winsound
obj = cv2.VideoCapture(0)
amount = 0
while(True):
    _,frame= obj.read()
    myqr = cv2.QRCodeDetector()
    v1, v2, v3 = myqr.detectAndDecode(frame)
    if(v1 != ''):
        if(v1 == 'banana'):
            amount+=100
            cv2.putText(frame,f'{v1} = {amount}',(50,60),cv2.FONT_ITALIC,2,(100,200,100),4)
            winsound.Beep(1000,500)
        if (v1 == 'cooking oil'):
            amount+=500
            cv2.putText(frame, f'{v1} = {amount}', (20, 60), cv2.FONT_HERSHEY_COMPLEX, 2, (200, 100, 200), 6)
            winsound.Beep(1000, 500)
    cv2.putText(frame, f'Price = {amount}', (100, 300), cv2.FONT_HERSHEY_COMPLEX, 2, (200, 100, 200), 6)
    cv2.imshow('IMAG1', frame)
    if(cv2.waitKey(200) == 27):
        break

obj.release()
cv2.destroyAllWindows()


