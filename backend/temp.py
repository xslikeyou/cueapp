import pymysql
from flask import Flask,request,jsonify
from flask_cors import CORS

# 数据库连接
db = pymysql.connect(host="127.0.0.1",
                     user="root",
                     password="112718",
                     db="myfavoriate",
                     charset='utf8mb4')
cursor=db.cursor()#数据库指针

#后端服务启动
app=Flask(__name__)
CORS(app,resources=r"/*")

@app.route("/url",methods=['POST'])#POST向服务器提交信息
def func():
    if request.method=='POST':
        username=request.form.get("username")
        print("收到用户名"+str(username))
        print("\n执行一些操作")
        return "返回给前端处理结果"
    
if __name__=="__main__":
    app.run( host='127.0.0.1',port=8899,debug=True)
    db.close()
    print("Good bye!")