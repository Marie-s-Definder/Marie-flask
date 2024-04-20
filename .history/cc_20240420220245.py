# import cv2

# # 读取现有图像
# image = cv2.imread("k61.jpg")

# # 定义矩形框的位置和大小
# x, y, w, h = 100, 50, 400, 300

# # 定义矩形框的颜色和透明度（蓝色，半透明）
# color = (255, 255, 255)  # 蓝色
#  # 透明度

# # 创建一个与图像大小相同的透明图像
# overlay = image.copy()

# # 绘制半透明矩形框
# cv2.rectangle(overlay, (x, y), (x + w, y + h), color, -1)

# # 将透明图像叠加到原始图像上
# alpha = 0.3
# cv2.addWeighted(overlay, alpha, image, 1 - alpha, 0, image)

# # 显示图像
# cv2.imshow("Transparent Rectangle", image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

my_dict = {'a': 4, 'b': 7, 'c': 2, 'd': 9}

sorted_dict = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))

top_three = dict(list(sorted_dict.items())[:3])

print(top_three)
