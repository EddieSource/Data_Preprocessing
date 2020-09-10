from __future__ import division
import cv2
import numpy as np
import open3d
import os
import sys

path = "C:\\Users\\Wei\\source\\repos\\MC_DataCollection\\MC_DataCollection\\test"

import matplotlib.pyplot as plt
# sys.path.append("C:\\Users\\Wei\\source\\repos\\MC_DataCollection\\MC_DataCollection\\test")
if not os.path.exists("pcd_data"):
    os.mkdir("pcd_data")


# img = cv2.imread(os.path.join(path, "depth\\" + str(38) + ".png"))
# cv2.imshow('img', img)
# cv2.waitKey(0)


#PreProcessing one image
# img_depth = cv2.imread("C:\\Users\\Wei\\source\\repos\\MC_DataCollection\\MC_DataCollection\\test\\depth\\" + "38" + ".png", -1)
# img_color = cv2.imread("C:\\Users\\Wei\\source\\repos\\MC_DataCollection\\MC_DataCollection\\test\\color\\" + "38" + ".png")



for index in range(0, 1000):
    img_depth = cv2.imread(os.path.join(path, "depth\\" + str(index) + ".png"), -1)
    img_color = cv2.imread(os.path.join(path, "color\\" + str(index) + ".png"))

    #double filter
    imgHSV = cv2.cvtColor(img_color, cv2.COLOR_BGR2HSV)
    for i in range(img_depth.shape[0]):
        for j in range(img_depth.shape[1]):
            if 640 < img_depth[i, j] < 700:
                if not (imgHSV[i, j][2] > 210):
                    img_depth[i, j] = 0
            else:
                img_depth[i, j] = 0

    # #normalize
    # max = float(img_depth.max())
    # min = float(img_depth.min())
    # plt.imshow((img_depth - min)/(max-min), cmap='gray')
    # plt.show()

    #res depth image to pcd and paint the pcd file
    camera_matrix = [612.311, 612.123, 639.191, 364.463] #fx, fy, cx, cy
    lst_depth = []
    lst_color = []
    for v in range(img_depth.shape[0]):
        for u in range(img_depth.shape[1]):
            if img_depth[v, u] != 0:
                z = img_depth[v, u]
                x = (u - camera_matrix[2]) / camera_matrix[0] * z
                y = (v - camera_matrix[3]) / camera_matrix[1] * z
                lst_depth.append([x, y, z])
                lst_color.append([img_color[v, u][2]/255, img_color[v, u][1]/255, img_color[v, u][0]/255])
    res_depth = np.array(lst_depth)
    res_color = np.array(lst_color)


    #create a pcd file
    pcd = open3d.geometry.PointCloud()
    pcd.points = open3d.utility.Vector3dVector(res_depth)
    # open3d.visualization.draw_geometries([pcd])


    pcd.colors = open3d.utility.Vector3dVector(res_color)
    open3d.io.write_point_cloud("pcd_data" + "\\" + str(index) + ".pcd", pcd)
    print(index, " collected")
    # open3d.visualization.draw_geometries([pcd])