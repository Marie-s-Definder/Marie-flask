import pickle
import docker
import time

def restart_container(container_name_or_id):
    try:
        container = client.containers.get(container_name_or_id)
        container.restart(timeout=20)
        print(f"容器 {container_name_or_id} 重启成功")
    except docker.errors.NotFound as e:
        print(f"找不到容器 {container_name_or_id}: {e}")
    except docker.errors.APIError as e:
        print(f"API 错误发生: {e}")
######

try:
    with open('Monitor.pkl', 'rb') as file:
        monitor = pickle.load(file)
    # Monitor = {'time': timeNow, 'successFlag': successFlag}
    LastTime = monitor['time']
    LastsuccessFlag = monitor['successFlag']

except Exception as e:
    print(f"wrong{e}")

client = docker.from_env()
print('正常运行')

while True:
    try:
        current_time_struct = time.localtime()
        # 格式化当前时间为字符串
        formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", current_time_struct)
        # 打印格式化后的当前时间
        print("当前时间:", formatted_time)


        with open('Monitor.pkl', 'rb') as file:
            monitor = pickle.load(file)
        # Monitor = {'time': timeNow, 'successFlag': successFlag}
        NowTime = monitor['time']
        NowsuccessFlag = monitor['successFlag']
        if NowTime/3600000-LastTime/3600000>= 5 or NowsuccessFlag==LastsuccessFlag==False:
            # 重启
            time.sleep(5)
            restart_container('mariee-flask-Using')
            time.sleep(5)
            restart_container('mariee-api')
            time.sleep(5)
            print(f'重启完成 NowTime={NowTime};NowsuccessFlag={NowsuccessFlag}')
        else:
            LastTime = NowTime
            LastsuccessFlag = NowsuccessFlag
            print(f'监听正常 NowTime={NowTime};NowsuccessFlag={NowsuccessFlag}')


    except Exception as e:
        print(f"wrong{e}")

    finally:
        time.sleep(2 * 60 * 60 )


