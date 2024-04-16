import cv2
import numpy as np
import matplotlib.pyplot as plt

# 读取彩色图像
image = cv2.imread('k61buttom.jpg')

# 将彩色图像转换为灰度图像
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 图像中心和旋转角度
center = (gray_image.shape[1] // 2, gray_image.shape[0] // 2)
angle = -20

# 旋转矩阵
rotation_matrix = cv2.getRotationMatrix2D(center, angle, 1.0)

# 指定填充颜色为白色
border_color = 0

# 进行图像旋转，并填充白色
rotated_image = cv2.warpAffine(gray_image, rotation_matrix, (gray_image.shape[1], gray_image.shape[0]),
                                borderMode=cv2.BORDER_CONSTANT, borderValue=border_color)

# print(rotated_image.shape)

sum_y = np.sum(rotated_image, axis=0)

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
cv2.imshow('Gray Image', rotated_image)

# 等待任意按键按下后关闭窗口
cv2.waitKey(0)
cv2.destroyAllWindows()
