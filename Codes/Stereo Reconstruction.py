# Stereo Reconstruction

import cv2 as cv
import numpy as np
from plyfile import PlyData, PlyElement #For ply file

imgL = cv.imread("D:/Samples/im0.png", 0)
imgR = cv.imread("D:/Samples/im1.png", 0)

size = imgL.shape[0],imgL.shape[1]

# To obtain the Disparity map

stereo = cv.StereoSGBM_create(numDisparities = 272, blockSize = 7)
disparity = stereo.compute(imgL, imgR)

imgL = cv.imread("D:/Samples/im0.png")
imgR = cv.imread("D:/Samples/im1.png")

plt.imshow(disparity, "jet") # To show the disparity  map
plt.show()
cv.waitKey(0)

# Parameters

cam0=np.array([[3979.911, 0, 1244.772],[0, 3979.911, 1019.507],[0, 0, 1]]) 
cam1=np.array([[3979.911, 0, 1369.115], [0, 3979.911, 1019.507], [0, 0, 1]])
doffs = 124.343
f=3927.911
b=193.001
Cx=1244.772
Cy=1019.507
width = 2964
height = 2000
ndisp = 270
isint = 0
vmin = 23
vmax = 245
dyavg = 0
dymax = 0
doffs = np.zeros((1,5)).astype(np.float32)

image3d = np.zeros((2000, 2964, 3))

Q = np.array([[1,0,0,-Cx],[0,1,0,-Cy],[0,0,0,f],[0,0,-1/b,doffs/b]]) # Perspective transformation matrix


print(disparity.dtype)
disparity = np.float32(disparity)/ndisp
print(disparity.dtype)

# Projecting the 3d points

image3d = cv.reprojectImageTo3D(disparity, Q, handleMissingValues= True)
colors = cv.cvtColor(imgR, cv.COLOR_BGR2RGB)

# Get rid of all the poiunts with value 0 (i.e those with no depth)
maskmap = disparity > disparity.min()

# Mask colors and points
outputpoints = image3d[maskmap]
outputcolors = colors[maskmap]

# Creating ply file
def create_point_cloud_file(vertices, colors, filename):
    colors =colors.reshape(-1,3)
    vertices = np.hstack([vertices.reshape(-1,3), colors])

    ply_header = '''ply 
        format ascii 1.0
        element vertex %(vert_num)d
        property float x
        property float y
        property float z
        property uchar red
        property uchar green
        property uchar blue
        end_header
        '''

    with open(filename, 'w') as f:
        f.write(ply_header %dict(vert_num = len(vertices)))
        np.savetxt(f, vertices, '%f %f %f %d %d %d')

outputfile = 'pointcloud10.ply' # To name it
create_point_cloud_file(outputpoints, outputcolors, outputfile) # To generate the point cloud file.
print("Done")