import requests
import json
import threading

def make_request(data):
    # 设置请求的头部
    headers = {
        'Content-Type': 'application/json'
    }

    # 发送 POST 请求到服务A
    url = 'http://localhost:5000/chatgpt'  # 替换为服务A的URL
    response = requests.post(url, headers=headers, data=json.dumps(data))

    # 获取响应数据
    response_data = response.json()

    # 处理响应数据
    print(response_data)

# 创建请求数据列表
request_data_list = [
    {'prompt': 'Hello', 'max_tokens': 10},
    {'prompt': 'Hi', 'max_tokens': 5},
    {'prompt': 'Greetings', 'max_tokens': 8},
    {'prompt': 'Greetings', 'max_tokens': 8},
    {'prompt': 'Greetings', 'max_tokens': 8},
    {'prompt': 'Greetings', 'max_tokens': 8},
    {'prompt': 'Greetings', 'max_tokens': 8},
    {'prompt': 'Greetings', 'max_tokens': 8},
    {'prompt': 'Greetings', 'max_tokens': 8},
    {'prompt': 'Greetings', 'max_tokens': 8}
]

# 创建并启动多个线程
threads = []
for data in request_data_list:
    thread = threading.Thread(target=make_request, args=(data,))
    thread.start()
    threads.append(thread)

# 等待所有线程执行完成
for thread in threads:
    thread.join()