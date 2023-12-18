import numpy as np
import cv2, time

cv2.namedWindow("Image Feed")
cap = cv2.VideoCapture(1)

count = 0
while True:
    ret, frame = cap.read()

    cv2.imshow("Image Feed", frame)

    # hit q to quit
    key = cv2.waitKey(1) & 0xFF
    if key == ord('s'):
        count += 1
        cv2.imwrite("realsense_imgN"+str(count)+".jpg", frame)
    if key == ord('q') or count >= 20:
        break

cap.release()
cv2.destroyAllWindows()

