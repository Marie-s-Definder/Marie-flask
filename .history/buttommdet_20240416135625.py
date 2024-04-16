import cv2

# 读取彩色图像
image = cv2.imread('k61buttom.jpg')

# 将彩色图像转换为灰度图像
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 显示原始图像和灰度图像
# cv2.imshow('Original Image', image)
cv2.imshow('Gray Image', gray_image)

# 等待任意按键按下后关闭窗口
cv2.waitKey(0)
cv2.destroyAllWindows()
