import requests
import json

# 请求的数据
data = {
    'prompt': 'Hello',
    'max_tokens': 10
}

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