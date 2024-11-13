# 使用官方 Python 3 镜像作为基础镜像
# FROM nvidia/cuda:12.4.1-cudnn-devel-ubuntu20.04
FROM python:3



# 将工作目录设置为 /app
WORKDIR /app

# 将当前目录下的所有文件（Dockerfile 所在目录）复制到 /app 中
COPY . /app

RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx
#RUN apt-get update && apt-get install -y pip

# 在镜像中安装 Python 应用所需的依赖
RUN pip install -r requirements.txt --default-timeout=100 alphabet -i https://pypi.tuna.tsinghua.edu.cn/simple torch

# 将容器的端口 80 暴露出来 //5000
EXPOSE 5000

# 运行应用
#CMD ["python", "main.py"]
#ENV FLASK_APP=main.py
#CMD ["flask", "run", "--host=0.0.0.0"]
