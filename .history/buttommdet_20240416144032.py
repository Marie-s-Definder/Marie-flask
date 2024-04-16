import cv2
import numpy as np
import matplotlib.pyplot as plt

# 读取彩色图像
image = cv2.imread('k61buttom.jpg')

# 将彩色图像转换为灰度图像
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 计算最小和最大像素值
min_pixel = np.min(gray_image)
max_pixel = np.max(gray_image)

# 线性变换
contrast_stretched = (255 / (max_pixel - min_pixel)) * (gray_image - min_pixel)

# 将像素值限制在 0 到 255 之间
contrast_stretched = np.clip(contrast_stretched, 0, 255).astype(np.uint8)

# 图像中心和旋转角度
center = (contrast_stretched.shape[1] // 2, gray_image.shape[0] // 2)

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
