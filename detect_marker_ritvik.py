"""
https://github.com/tizianofiorenzani/how_do_drones_work/blob/master/opencv/aruco_pose_estimation.py
https://www.youtube.com/watch?v=CmDO-w56qso 
"""

import numpy as np
import cv2
import cv2.aruco as aruco
import csv


filename = "testfile.csv"
fields = ["x (cm)", "y (cm)", "z (cm)"]

# tag properties
marker_size = 17.7
marker_id = 72

# camera properties
with open("realSenseCal.npy", "rb") as f:
    camera_matrix = np.load(f)
    camera_distortion = np.load(f)

# define aruco dictionary
# aruco_dict = aruco.getPredefinedDictionary(aruco.DICT_6X6_250)
aruco_dict  = aruco.getPredefinedDictionary(aruco.DICT_ARUCO_ORIGINAL)
parameters  = aruco.DetectorParameters_create()
parameters.adaptiveThreshConstant = 10

cap = cv2.VideoCapture(1)

with open(filename, 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)

    while True:
        ret, frame = cap.read()
        # cv2.imshow("frame", frame)
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        corners, ids, rejected = aruco.detectMarkers(image=gray_frame, dictionary=aruco_dict, parameters=parameters, 
                                        cameraMatrix=camera_matrix, distCoeff=camera_distortion)

        if ids is not None:
            # print(ids[0])
            aruco.drawDetectedMarkers(frame, corners)
            ret = aruco.estimatePoseSingleMarkers(corners, marker_size, camera_matrix, camera_distortion)

            rvec, tvec = ret[0][0,0,:], ret[1][0,0,:]

            aruco.drawDetectedMarkers(frame, corners)
            aruco.drawAxis(frame, camera_matrix, camera_distortion, rvec, tvec, 10)
            
            addRow = [tvec[0], tvec[1], tvec[2]]
            csvwriter.writerow(addRow)

            str_position = "MARKER Position x=%4.0f  y=%4.0f  z=%4.0f"%(tvec[0], tvec[1], tvec[2])
            cv2.putText(frame, str_position, (0, 100), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 2, cv2.LINE_AA)

        cv2.imshow("frame", frame)
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
