from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/chatgpt', methods=['POST'])
def process_request():
    # 获取请求数据
    request_data = request.get_json()

    # 向 OpenAI GPT-3 API 发送请求
    api_key = 'YOUR_API_KEY'  # 替换为你的 OpenAI API 密钥
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + api_key
    }
    data = {
        'prompt': request_data['prompt'],
        'max_tokens': request_data['max_tokens']
    }
    # response = requests.post('https://api.openai.com/v1/engines/davinci-codex/completions', headers=headers, json=data)
    # response_data = response.json()

    # 返回响应数据给后端的 glong 程序
    response = jsonify({'response': 'Hello from Flask!'})   
    return response
    # return jsonify(response_data)

if __name__ == '__main__':
    app.run()
