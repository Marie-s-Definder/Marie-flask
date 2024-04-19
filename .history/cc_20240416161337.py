import cv2

# 读取现有图像
image = cv2.imread("k61.jpg")

# 定义矩形框的位置和大小
x, y, w, h = 100, 50, 400, 300

# 定义矩形框的颜色和透明度（蓝色，半透明）
color = (255, 255, 255)  # 蓝色
alpha = 0.89 # 透明度

# 创建一个与图像大小相同的透明图像
overlay = image.copy()

# 绘制半透明矩形框
cv2.rectangle(overlay, (x, y), (x + w, y + h), color, -1)

# 将透明图像叠加到原始图像上
cv2.addWeighted(overlay, alpha, image, 1 - alpha, 0, image)

# 显示图像
cv2.imshow("Transparent Rectangle", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
