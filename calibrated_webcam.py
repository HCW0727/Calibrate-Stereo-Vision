import cv2
import numpy as np

webcam = cv2.VideoCapture(0)
middle_w = int(webcam.get(3)/2)

####################################################################################

l_mtx = np.array([[1.36688831e+03 ,0.00000000e+00 ,5.42896031e+02],
 [0.00000000e+00 ,1.37042747e+03 ,3.87374004e+02],
 [0.00000000e+00 ,0.00000000e+00 ,1.00000000e+00]])

l_newCameramtx = np.array([[1.16126453e+03 ,0.00000000e+00 ,5.20710207e+02],
 [ 0.00000000e+00 ,1.13378918e+03 ,3.87108333e+02],
 [0.00000000e+00 ,0.00000000e+00 ,1.00000000e+00]])

l_dist = np.array([[-4.50195983e-01  ,2.29675267e-01 ,-1.34943624e-03  ,9.91683482e-05, 8.18452763e-03]])

#x,y,w,h
l_roi = (22, 54, 1228, 616)

####################################################################################

r_mtx = np.array([[1.36922572e+03 ,0.00000000e+00 ,6.76968838e+02],
 [0.00000000e+00 ,1.36635145e+03 ,3.34266442e+02],
 [0.00000000e+00 ,0.00000000e+00 ,1.00000000e+00]])

r_newCameramtx = np.array([[1.17232092e+03 ,0.00000000e+00 ,6.85258002e+02],
 [0.00000000e+00 ,1.15809595e+03 ,3.33400673e+02],
 [0.00000000e+00 ,0.00000000e+00 ,1.00000000e+00]])

r_dist = np.array([[-4.34075416e-01  ,2.04086358e-01 ,1.70629664e-03 ,-3.54754716e-04 ,-1.60347753e-02]])

#x,y,w,h
r_roi = (30, 42, 1224, 630)

####################################################################################

num = 0

while webcam.isOpened():
    status,frame = webcam.read()
    left = frame[:,middle_w:]
    right = frame[:,:middle_w]

    left = cv2.undistort(left,l_mtx, l_dist, None, l_newCameramtx)
    x,y,w,h = l_roi
    left = left[y:y+h, x:x+w]

    right = cv2.undistort(right,r_mtx, r_dist, None, r_newCameramtx)
    x,y,w,h = r_roi
    right = right[y:y+h, x:x+w]

    cv2.imshow('left',left)
    cv2.imshow('right',right)

    k = cv2.waitKey(100)

    if k == 27:
        break

    elif k == ord('s'):
        cv2.imwrite('left' + str(num) + '.png',left)
        cv2.imwrite('right.png',right)
        print("images saved!")

        num += 1

    

webcam.release()
cv2.destroyAllWindows()