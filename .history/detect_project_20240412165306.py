from ultralytics import YOLO
import math
import cv2

# Load a model
# model = YOLO('/root/autodl-tmp/yolov8/ultralytics/models/v8/yolov8m-IAT.yaml') # build a new model from scratch
def yolov8m(img, \
            preset_boxes= [[10, 10, 100, 100],  # 预置框1，左上角坐标 (10, 10)，右下角坐标 (100, 100)
                [150, 50, 250, 150],  # 预置框2，左上角坐标 (150, 50)，右下角坐标 (250, 150)
                [300, 200, 400, 300],  # 预置框3，左上角坐标 (300, 200)，右下角坐标 (400, 300)
                [50, 300, 150, 400],  # 预置框4，左上角坐标 (50, 300)，右下角坐标 (150, 400)
                [200, 100, 300, 200],  # 预置框5，左上角坐标 (200, 100)，右下角坐标 (300, 200)
                [350, 50, 450, 150]  # 预置框6，左上角坐标 (350, 50)，右下角坐标 (450, 150)
            ],   \
            pt = 'best.pt'):
    # path = "liandbu.jpg"
    model = YOLO(pt)  # load a pretrained model (recommended for training)
    # model = YOLO('/root/autodl-tmp/yolov8/ultralytics/models/v8/yolov8m-enhance.yaml').load('/root/autodl-tmp/yolov8/yolov8m.pt')
    # Use the model
    # img = cv2.imread(path)
    detections = model.predict(source=img, save=False)  # train the model
    # print(detections)
    # print('yes')

    output = [True, True, True, False, True, False]
    # print(detections)

    # 定义匹配阈值
    threshold = 400  # 这个阈值需要根据具体情况进行调整
    # print(detections[0].boxes)
    # print(len(detections))
    boxesList = []
    # print(detections[0])
    for item in detections[0].boxes:
        boxesList.append(item.xyxy.squeeze())
    # boxesList = sorted(boxesList, key=lambda b: (b[1], b[0]))
    lines = sorted(boxesList, key=lambda b: (b[1]))
    lineOne = lines[:3]
    lineTwo = lines[3:6]
    # lineOne = sorted(lineOne, key=lambda b: (b[0]))
    # lineTwo = sorted(lineTwo, key=lambda b: (b[0]))
    boxesList = sorted(lineOne, key=lambda b: (b[0])) + sorted(lineTwo, key=lambda b: (b[0]))
    # print(len(boxesList))
    # for i, preset_box in enumerate(preset_boxes):        
    #     # 计算预置框的中心点坐标
    #     preset_center_x = (preset_box[0] + preset_box[2]) / 2
    #     preset_center_y = (preset_box[1] + preset_box[3]) / 2

    for boxIndex, detection_box in enumerate(boxesList):
        # 1白色：(255, 255, 255)
        # 2黑色：(0, 0, 0)
        # 3红色：(0, 0, 255)
        # 4绿色：(0, 255, 0)
        # 5蓝色：(255, 0, 0)
        # 6黄色：(0, 255, 255)
        # 品红色（洋红色）：(255, 0, 255)
        # 青色：(255, 255, 0)
        # if boxIndex == 0:
        #     color = (255, 255, 255)
        # elif boxIndex == 1:
        #     color = (0, 0, 0)
        # elif boxIndex == 2:
        #     color = (0, 0, 255)
        # elif boxIndex == 3:
        #     color = (0, 255, 0)
        # elif boxIndex == 4:
        #     color = (255, 0, 0)
        # elif boxIndex == 5:
        #     color = (0, 255, 255)
        # cv2.rectangle(img, (int(detection_box[0]),int(detection_box[1])), (int(detection_box[2]),int(detection_box[3])), color, 2)
        
        # print(detections[0].boxes)
        # 计算检测结果框的中心点坐标
        # detection_box = detection_box
        # detection_box = detection_box.xyxy.squeeze()
        # print(detection_box)
        detection_center_x = (detection_box[0] + detection_box[2]) / 2
        detection_center_y = (detection_box[1] + detection_box[3]) / 2
        # print(len(preset_boxes))
        # 计算中心点之间的距离
        # print(boxIndex)
        preset_center_x = (preset_boxes[boxIndex][0] + preset_boxes[boxIndex][2]) / 2
        preset_center_y = (preset_boxes[boxIndex][1] + preset_boxes[boxIndex][3]) / 2
        distance = math.sqrt((detection_center_x - preset_center_x) ** 2 + (detection_center_y - preset_center_y) ** 2)
        # print(distance)
        # 如果距离小于阈值，则认为是匹配的框
        if distance < threshold:
            # print('2')
            output[boxIndex] = not output[boxIndex]
    # cv2.imshow('a',img)
    # cv2.waitKey()
        # 删除已经比对的元素
        # boxesList.pop(boxIndex)
        # else:
        #     print('no')
        # print(a)
                
    return output, preset_boxes
    # 输出匹配结果数组
    # print(output)
# yolov8m()
