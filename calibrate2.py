import numpy as np
import cv2
import glob

chessboardsize = (9,6)
frameSize = (1920,1080)


# termination criteria
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)


# prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
objp = np.zeros((chessboardsize[0] * chessboardsize[1],3), np.float32)
objp[:,:2] = np.mgrid[0:chessboardsize[0],0:chessboardsize[1]].T.reshape(-1,2)
# Arrays to store object points and image points from all the images.
objpoints = [] # 3d point in real world space
imgpoints = [] # 2d points in image plane.
# images = glob.glob('right/*.png')
images = glob.glob('*.png')
for fname in images:
    img = cv2.imread(fname)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    # cv2.imshow('test',gray)
    # cv2.waitKey(0)
    # Find the chess board corners
    ret, corners = cv2.findChessboardCorners(img, (9,7),None)
    # If found, add object points, image points (after refining them)

    print(ret)
    if ret == True:
        objpoints.append(objp)
        corners2 = cv2.cornerSubPix(gray,corners,(11,11),(-1,-1),criteria)
        imgpoints.append(corners2)
        # Draw and display the corners
        img = cv2.drawChessboardCorners(img, (7,6), corners2,ret)
        
cv2.destroyAllWindows()

ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1],None,None)

img = cv2.imread(images[0])
h,  w = img.shape[:2]
newcameramtx, roi=cv2.getOptimalNewCameraMatrix(mtx,dist,(w,h),1,(w,h))

print('mtx : ',mtx)
print('newcameramtx', newcameramtx)

# dst = cv2.undistort(img, mtx, dist, None, newcameramtx)
# x,y,w,h = roi
# dst = dst[y:y+h, x:x+w]
# cv2.imwrite('calibresult.png',dst)

print('roi : ',roi)
print('dist : ',dist)

#new camera mtx , dist, mtx, roi 저장해두기