from random import sample
import cv2
import numpy as np
import random
import math
import datetime

pname, ptype = 0, 0


class Bottom():
    def __init__(self):
        self.pic = None

    def angle(self, v1, v2):
        dx1 = v1[2] - v1[0]
        dy1 = v1[3] - v1[1]
        dx2 = v2[2] - v2[0]
        dy2 = v2[3] - v2[1]
        angle1 = math.atan2(dy1, dx1)
        angle1 = angle1 * 180 / math.pi

        print('angle1', angle1)
        angle2 = math.atan2(dy2, dx2)
        angle2 = angle2 * 180 / math.pi
        print('angle2', angle2)
        if angle1 * angle2 >= 0:
            if angle2 <= 0 and angle2 >= -90:
                included_angle = abs(angle1 - angle2)
            else:
                included_angle = 360 - abs(angle1 - angle2)
        else:
            included_angle = abs(angle1) + abs(angle2)
        return included_angle


    def linecontours(self, cp_info):
        """
        :funtion : 提取刻度线，指针
        :param a: 高斯滤波 GaussianBlur，自适应二值化adaptiveThreshold，闭运算
        :param b: 轮廓寻找 findContours，
        :return:kb,new_needleset
        """
        r_1, c_x, c_y = cp_info
        # 高斯滤波
        img = cv2.GaussianBlur(self.pic, (3, 3), 0)
        # img = self.pic
        # 转换为灰度图
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        binary = cv2.adaptiveThreshold(~gray, 255,
                                       cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 7, -6)
        

        maskImg = np.zeros((img.shape[0], img.shape[1]), dtype=np.uint8)
        radius = int((img.shape[0] if img.shape[1]>img.shape[0] else img.shape[1])*1/3)
        cv2.circle(maskImg, (int(img.shape[1]/2), int(img.shape[0]/2)), radius, 255, -1)
        binary = cv2.bitwise_and(binary, maskImg)
        # cv2.imshow("binary", binary)
        # cv2.waitKey()
        # 3/6 2/6
        # 6/12 4/12
        # 12/24 8/24
        # 闭运算
        kernel = np.ones((3, 3), np.uint8)
        binary = cv2.dilate(binary, kernel, iterations=1)
        # cv2.imshow("binary", binary)
        # cv2.waitKey()

        # lines = cv2.HoughLinesP(binary, 1, np.pi / 180, 1, minLineLength=int(img.shape[0] / 8), maxLineGap=2)
        # nmask = np.zeros(binary.shape, np.uint8)
        
        # for line in lines:
        #     x1, y1, x2, y2 = line[0]
        #     # cv2.imshow("binary", nmask)
        #     # cv2.waitKey()
        #     cv2.line(nmask, (x1, y1), (x2, y2), 100, 2, cv2.LINE_AA)
        # cv2.imshow("binary", nmask)
        # cv2.waitKey()
        # nmask = cv2.erode(nmask, kernel, iterations=1)
        cnts, _ = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
        # cv2.drawContours(img, cnts, -1, (0, 255, 0), 2)

        # # 显示绘制了轮廓的图像
        # cv2.imshow("Contours", img)
        # cv2.waitKey()

        x1 = 0
        x2 = img.shape[1]
        areass = [cv2.contourArea(x) for x in cnts]
        i = areass.index(max(areass))
        cnt = cnts[i]
        output = cv2.fitLine(cnt, 2, 0, 0.001, 0.001)
        k = output[1] / output[0]
        k = round(k[0], 2)
        b = output[3] - k * output[2]
        b = round(b[0], 2)
        y1 = int(k * x1 + b)
        y2 = int(k * x2 + b)
        # print(k)
        
        cv2.line(img, (x1, y1), (x2, y2), (0, 23, 255), 1, cv2.LINE_AA)
        # cv2.imshow("Contours", img)
        # cv2.waitKey()
        # cv2.imshow("binary", img)
        # cv2.waitKey()
        if x1 >= x2:
            xmax, xmin = x1, x2
        else:
            xmax, xmin = x2, x1

        if  y1 >= y2:
            ymax, ymin = y1, y2
        else:
            ymax, ymin = y2, y1
        # xmax, xmin = x1, x2 if x1 >= x2 else x2, x1
        # ymax, ymin = y1, y2 if y1 >= y2 else y2, y1

        # 只需要变化y即可知道角度，因此无需对x进行修改
        return xmin, xmax, ymin, ymax


    def angle_with_horizontal(self, line):
        # line = [xmin, xmax, ymin, ymax]
        xmin, xmax, ymin, ymax = line
        # angle_rad = np.arctan2(y1 - y2, x1 - x2)
        # angle_deg = np.degrees(angle_rad)
        dx = xmax - xmin
        dy = ymax - ymin
        angle_rad = np.arctan2(dy, dx)
        angle_deg = np.degrees(angle_rad)
        # angle_deg = angle_deg if angle_deg>=0 else angle_deg + 180
        return angle_deg if angle_deg>=0 else angle_deg + 180



    def decter(self, image):

        # start = datetime.datetime.now()
        # 霍夫圆的圆心位置和半径

        # ninfo = self.cut_pic(image)  # 2.截取表盘
        ninfo = [1, 2, 2]
        self.pic = image
        # cv2.imshow("image", image)
        # cv2.waitKey(5000)
        xmin, xmax, ymin, ymax = self.linecontours(ninfo)  # 提取刻度线、指针
        OZ = [xmin, xmax, ymin, ymax]
        angle1 = self.angle_with_horizontal(OZ)
        # print("与水平线的夹角：", angle1)
        # end = datetime.datetime.now()
        # print(end - start)
        # cv2.waitKey(1)
        
        print(f"angle:{angle1}")
        if angle1 > 0 and angle1 < 77:
            return "自动", 0
            return "自动"
        if angle1 > 77 and angle1 < 112:
            return "停", 2
            return "停"
        if angle1 > 112:
            return "手动", 1
            return "手动"


if __name__ == "__main__":
    # 输入文件夹
    inputpath = 'input/bottom/5.jpg'
    aa = Bottom()
    image = cv2.imread(inputpath)
    status = aa.decter(image)
    print("检测结果：", status)

