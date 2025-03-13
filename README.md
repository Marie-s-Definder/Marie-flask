# Marie-flask

## 各个文件作用
- Monitor.py
  - 用于监视flask容器是否出问题
  - 当连续5h状态没有更新，或者连续5h都处于报错状态就会重启flask容器
- detect_project.py
  - yolov8检测，在旋钮检测和灯检测都会用到
  - 旋钮检测会直接返回一个旋钮的位置
  - 灯光检测会返回6个灯的位置
- bottomReal.py
  - 旋钮检测，直接返回 “自动” “停” “手动” 三种状态
- simsun.ttc 字体文件
- 输入示例json
  - 后端给flask的输入json示例，若系统重构可以参考
- dockerfile
  - dockerfile
- main.py
  - 识别程序的主文件
- **其他文件都暂时没用**

- 几个docker的run指令
```

docker run -d --name mariee-api -v /home/marie/Mariee0331/data:/app/data -p 8080:8080 mariee-api:latest

docker run --gpus all -v /home/marie/Mariee0331/data:/app -p 5000:5000 -itd --name mariee-flask-Using flask python /app/main.py

docker run -d --name mariee-web-admin -p 90:80 mariee-web-admin:latest

```
