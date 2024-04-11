from flask import Flask, request
from detect_project import yolov8m
from bottomReal import Bottom
from meter_single import Meter
import datetime

import cv2
BottomDet = Bottom()
meterDet  = Meter()
app = Flask(__name__)

@app.route('/Recognition', methods=['POST'])
def Recognition():
    data = request.json
    url = data.get('url')
    data = data.get('data')
    try:
        pic = cv2.imread(url)
    except:
        return "Wrong Url"
    savingurl = url+'ppp'
    returndata = {"url":savingurl}
    dataList = []
    for item in data:
        dataa = {}
        Id = item['id']
        if item['item'] == 'buttom':
            pass
        elif item['item'] == 'light':
            pass
        elif item['item'] == 'meter':
            image = slide(pic, item['location'])
            # 获取角度
            ang = meterDet.decter(image, item['zeroPoint'])
            # 获取时间戳
            timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            # 获取状态
            if ang>=item['lowerLimit'] and ang<=item['upperLimit']:
                status = 0
            else:
                status = 1
            
        elif item['item'] == 'iot':
            pass
        else:
            return f"Wrong Type {Id}"
    return f'Hello, {url}!'

def slide(image,xl,yl,xb,yb):
    return image[xl:xb,yl:yb]


if __name__ == '__main__':
    app.run(debug=True)
