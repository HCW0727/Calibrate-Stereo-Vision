import cv2

webcam = cv2.VideoCapture(0)

middle_w = int(webcam.get(3)/2)

num = 0

while webcam.isOpened():

    status, frame = webcam.read()
    left = frame[:,middle_w:]
    right = frame[:,:middle_w]


    k = cv2.waitKey(5)

    if k == 27:
        break
    
    elif k == ord('s'): # wait for 's' key to save and exit
        cv2.imwrite('left' + str(num) + '.png', left)
        # cv2.imwrite('right' + str(num) + '.png', right)
        print("images saved!")
        num += 1

    cv2.imshow('Img 1',left)
    # cv2.imshow('Img 2',right)

# Release and destroy all windows before termination
webcam.release()

cv2.destroyAllWindows()