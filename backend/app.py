from flask import Flask, request, jsonify
from flask_cors import CORS
from openai import OpenAI
 
client = OpenAI(
    api_key = "sk-V5vPoqFdxtzmtPOqKf5OlRi2C8Vpzv4slZyQ9051ZiiOkxae",
    base_url = "https://api.moonshot.cn/v1",
)
 

 
#后端服务启动
app=Flask(__name__)
CORS(app,resources=r"/*")

@app.route('/answer', methods=['POST'])
def get_answer():
    question = request.json.get('question')
    completion = client.chat.completions.create(
    model = "moonshot-v1-8k",
    messages = [
        {"role": "system", "content": "你是 Kimi，由 Moonshot AI 提供的人工智能助手，你更擅长中文和英文的对话。你会为用户提供安全，有帮助，准确的回答。同时，你会拒绝一切涉及恐怖主义，种族歧视，黄色暴力等问题的回答。Moonshot AI 为专有名词，不可翻译成其他语言。"},
        {"role": "user", "content": question}
    ],
    temperature = 0.3,
    )
    
    # 这里只是一个示例答案
    answer = f"{completion.choices[0].message.content}"
    print(answer)
    return jsonify({"answer": answer})

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=8899)