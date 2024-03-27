"""
 @author: sizhong
 @date: 2024-01-10
 @File: demo.py
 @Description: 
"""

# laspy
# 文档：https://laspy.readthedocs.io/en/latest/installation.html


import laspy
import numpy as np

# 示例数据
points = [
    [110.086100, 39.855400, 100],
    [110.083500, 39.855000, 200],
    [110.084759395508, 39.852656725581, 300]
]

# 创建一个新的 LAS 文件
header = laspy.LasHeader(version="1.4", point_format=3)
las = laspy.LasData(header)

# 准备数据
x_values = np.array([point[0] for point in points], dtype=np.float64)
y_values = np.array([point[1] for point in points], dtype=np.float64)
z_values = np.array([point[2] for point in points], dtype=np.float64)
intensity_values = np.array([point[3] for point in points], dtype=np.uint16)

# 赋值给 las 对象
las.x = x_values
las.y = y_values
las.z = z_values
las.intensity = intensity_values

# 将数据写入文件
las.write("output.las")
