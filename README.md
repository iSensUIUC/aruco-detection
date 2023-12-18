# aruco-detection
Pose estimation of a drone using an Aruco Marker placed within camera view


## Camera Calibration
In order for the openCV function to correctly estimate the pose of the marker relative to the camera, it must first account for the distortion of the camera. 

The script calibrate_cam.py uses the images taken from the Intel RealSense Depth Camera (pictures taken via capture_image.py and stored in calibration_img folder) to calculate the camera distortion matrices and store them in the file realSenseCal.npy. If using a different camera, new pictures would need to be taken and calibrate_cam.py would need to be run once before running the pose estimation scripts.

NOTE: If the camera calibration is bad, the pose estimates will be bad.

## Pose Estimation
This is done via the detect_marker.py script. It reads the calibration matrices stored in realSenseCal.npy and uses those as inputs to the cv2.aruco.detectMarkers() function to determine the location of all markers in the frame.

## How to run
Step 1: Run calibrate_cam.py with the correct calibration images for your camera. This only needs to be done once.

Step 2: Keep the marker within camera view and run detect_marker.py. This will store a steady stream of [x,y,z] coordinates in a csv file.

