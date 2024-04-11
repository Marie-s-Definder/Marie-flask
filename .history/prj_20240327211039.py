from flask import Flask, request
from detect_project import yolov8m
from meter import Meter

import cv2
meterDet = Meter()
app = Flask(__name__)

@app.route('/Recognition', methods=['POST'])
def Recognition():
    data = request.json
    url = data.get('url')
    data = data.get('data')
    print(url)

    print(data[0])
    return f'Hello, {url}!'


if __name__ == '__main__':
    app.run(debug=True)
