import cv2
import numpy as np



img = cv2.imread('D:/DataSource/Python/opencv-test/michael_jordan_1998.jpg')

cv2.imshow('jordan', img)

cv2.waitKey(0)
cv2.destroyAllWindows()

'''test'''
# if __name__ == '__main__':
#    cam = cv2.VideoCapture(0)
#    while True:
#        ret, img = cam.read()
#        vis = img.copy()
#        cv2.imshow('facedetect', vis)
#        if 0xFF & cv2.waitKey(5) == 27:
#            break
# cv2.destroyAllWindows()