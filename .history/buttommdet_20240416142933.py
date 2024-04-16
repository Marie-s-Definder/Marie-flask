import cv2
import numpy as np
import matplotlib.pyplot as plt

# 读取彩色图像
image = cv2.imread('k61buttom.jpg')

height, width = image.shape[:2]

# 计算旋转中心，这里选择图像中心
center = (width // 2, height // 2)

# 设置旋转角度（逆时针90度）
angle = -40

# 获取旋转矩阵
rotation_matrix = cv2.getRotationMatrix2D(center, angle, 1.0)

# 应用旋转矩阵进行旋转
rotated_image = cv2.warpAffine(image, rotation_matrix, (width, height))

# 将彩色图像转换为灰度图像
gray_image = cv2.cvtColor(rotated_image, cv2.COLOR_BGR2GRAY)

sum_y = np.sum(gray_image, axis=0)

# 绘制图像
plt.figure(figsize=(10, 5))
plt.plot(sum_y, color='b')
plt.title('Sum Along Y-axis')
plt.xlabel('X-coordinate')
plt.ylabel('Sum of Pixel Values')
plt.grid()
plt.show()

# 显示原始图像和灰度图像
# cv2.imshow('Original Image', image)
cv2.imshow('Gray Image', gray_image)

# 等待任意按键按下后关闭窗口
cv2.waitKey(0)
cv2.destroyAllWindows()
