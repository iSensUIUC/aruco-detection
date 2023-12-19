# Description of Testing Data
Static and Dynamic tests were run to verify the accuracy of the Aruco pose estimation from 1m upto 10m

## Static Tests
This involved placing the camera at the same position relative to the marker at all times and increasing the distance along the same axis every time. From 1m to 10m, the pose estimation code was run until a sufficient amound of data was collected and then the distance was increased. 

This data is stored in distXm.csv.

## Dynamic Tests
After each static test was conducted, a moving test was conducted at the same distance. This time, as data was being collected, the camera was moved back and forth a distance of 15 cm along an axis perpendicular to the distance being measured.

This data is stored in distXm_mov15.csv.

