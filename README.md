# Stereo-Reconstruction

Stereo reconstruction is the concept of realization of depth from a pair of stereo images.

### What are stereo images?

Stereo images are two images of the same object such that, they have parallel or slightly verged image planes.

### What are we trying to achieve with stereo reconstruction?

Stereo reconstruction is used primarily in entertainment and/or 3D modelling.
We are trying to obtain a usable point cloud from a pair of stereo images.

### Status of the project : 

Currently the project includes disparity map and pointcloud obtained from one dataset.

Note : Code to obtain the disparity map can be found in the "codes" directory.

### Parameters and stereo geometry : 

What are camera parameters and the intrinsic matrix?

![](https://i.imgur.com/QuIZ7Y6.png)

The above matrix is called the **intrinsic camera matrix** which provides us with the camera parameters, where

fx is the focal length of the camera,
fy is given as fy = a fx, where a is the aspect ratio and
Cx and Cy are the offsets.

**Relation between the depth and disparity** :

![](https://i.imgur.com/m3PkWkx.png)

Applying similarity of triangles on the above diagram, we obtain the relation as

**Disparity = x - x' = Bf/Z**

Where Z refers to the z coordinate or depth of the image. And f is the focal length.

**Projections and transformations** : 
1. Translation
2. Euclidean transformation
3. Similarity transformation
4. Affine transformation and
5. Projective transformation

To know more about the transformations, you can check out https://youtu.be/91eroryYZno

**Perpective transformation matrix** : 

![](https://i.imgur.com/3DrIuaw.png)

The above matrix is called the perspective projection matrix, which is a necessary parameter in the reprojectImageTo3D function of openCV.

Where Cx and Cy are offsets,
f is the focal length of camera,
Tx is the baseline,
Cx-Cx' is the difference of offsets.

### Some important terms : 

**Disparity map** : Disparity map refers to a mapping of the apparent shift or pixel difference of points in the two images.
 
**Perspective transformation matrix** : It is the matrix that is used to obtain the point in the image plane from a point in 3D. It takes in parameters of the camera and the baseline into account.

**Point cloud** : Point cloud is a set of all the points in any object.

### What are the steps that we need to follow?

1. Creating a disparity map from the two stereo images.
2. Obtain the perpective projection matrix from camera parameters.
3. Obtain the pointcloud from the disparity map using the reprojectImageTo3D function of openCV.
4. Visualise the pointcloud.(through meshlab in this case)

### Tools and softwares needed to perform the project : 

Coding was entirely done in python and the following libraries were used : 
1. The Numpy libray
2. The OpenCV library
3. The plyfile library

### Results : 

![](https://i.imgur.com/0wtSrVQ.jpg)

The above is the result of the algorithm to obtain the disaprity map.

![](https://i.imgur.com/GYaws28.gif)

The above is the visualization of the pointcloud obtained.


**Credits** :
The explanation on stereo geometry was referenced from OpenCV tutorials.
https://docs.opencv.org/4.5.2/dd/d53/tutorial_py_depthmap.html
