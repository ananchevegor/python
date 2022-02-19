# распознавание лиц
import cv2

def webcamera():

    cam = cv2.VideoCapture(0)

    while True:
        ret, img = cam.read()
        cv2.imshow('camera', img)
        if cv2.waitKey(10) == 27:
            break
    cam.realise()
    cv2.destroyAllWindows()

webcamera()