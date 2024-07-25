from flask import Flask, request, jsonify
from flask_cors import CORS

#后端服务启动
app=Flask(__name__)
CORS(app,resources=r"/*")

@app.route('/answer', methods=['POST'])
def get_answer():
    question = request.json.get('question')
    # 这里只是一个示例答案
    answer = f"The answer to '{question}' is not found in the database."
    print(answer)
    return jsonify({"answer": answer})

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=8899)