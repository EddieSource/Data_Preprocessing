# Data_Preprocessing

Main.py includes three parts of code: Color filtering, depth filtering, and conversion from RGB-D image to point cloud data. 
The conversion is based on three formulas: 
  for each point: 
  z = d
  x = (u - cx) / fx * z
  y = (v - cy) / fy * z

where cx, cy, fx, fy are the camera intrinsics

The point cloud data was then colored and stored. It will be matched with internal images and processed later. 
