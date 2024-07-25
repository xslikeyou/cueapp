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

@app.route("/login/list",methods=['POST'])#POST向服务器提交信息
def login_list():
    if request.method=='POST':
        cursor.execute("SELECT id,username,role,ctime FROM login")
        data=cursor.fetchall()
        result=[]
        if data!=None:
            for i in data:
                temp={}
                temp['id']=i[0]
                temp['username']=i[1]
                temp['role']=i[2]
                temp['ctime']=i[3]
                result.append(temp)
            print(result,len(result))
            return jsonify(result)
        else:
            print("result:NULL")
            return jsonify([])

@app.route("/login/add",methods=['POST'])#POST向服务器提交信息       
def login_add():
    if request.method=='POST':
        username=request.form.get("username")
        password=request.form.get("password")
        role=request.form.get("role")
        cursor.execute("SELECT id,username,role,ctime FROM login")
        try:
            cursor.execute("INSERT INTO login(username, password,role)VALUES(\""+str(username)+"\",\""+str(password)+"\","+str(role)+") ")
            db.commit()
            print("add a new user successfully")
            return "1"
        except Exception as e:
            print('add a new user failed:',e)
            db.rollback()
            return "-1"
        

@app.route("/login/del",methods=['POST'])#POST向服务器提交信息
def login_del():
    if request.method=='POST':
           id=request.form.get("id")
           try:
               cursor.execute("DELETE FROM login WHERE id="+str(id))
               db.commit()
               print("delete a user successfully")
               return "1"
           except Exception as e:
               print('delete a user failed:',e)
               db.rollback()
               return "-1"

@app.route("/login/update",methods=['POST'])#POST向服务器提交信息
def login_update():
    if request.method=='POST':
           id=request.form.get("id")
           password=request.form.get("password")
           try:
               cursor.execute("UPDATE login SET password=\""+str(password)+"\" where id="+str(id))
               db.commit()
               print("delete a user successfully")
               return "1"
           except Exception as e:
               print('delete a user failed:',e)
               db.rollback()
               return "-1"
           
@app.route("/login/login",methods=['POST'])#POST向服务器提交信息
def login_login():
    if request.method=='POST':
        username=request.form.get("username")
        password=request.form.get("password")
        cursor.execute("SELECT id,username, role,ctime FROM login WHERE username=\'"+str(username)+"\' AND password=\'"+str(password)+"\'")
        data=cursor.fetchone()
        if data!=None:
            print('result:',data)
            jsondata={"id":str(data[0]),"username":str(data[1]),"role":str(data[2]),"ctime":str(data[3])}
            return jsonify(jsondata)
        else:
            print("result:NULL")
            return jsonify({})
        
@app.route("/favorite/update",methods=['POST'])#POST向服务器提交信息
def favorite_update():
    if request.method=='POST':
        id=request.form.get("id")
        wname=request.form.get("id")
        wurl=request.form.get("id")
        _type=request.form.get("type")
        try:
            cursor.execute("UPDATE favorite SET wname=\'"+str(wname)+"\',wurl=\'"+str(wurl)+"\',type=\'"+str(_type)+"\' WHERE id=\'"+str(id)+"\'")
            db.commit()
            print('update favorite successfully')
            return "1"
        except Exception as e:
            print('update favorite failed:',e)
            db.rollback()
            return "-1"
        
@app.route("/favorite/count",methods=['POST'])#POST向服务器提交信息
def favorite_count():
    if request.method=='POST':
        id=request.form.get("id")
        try:
            cursor.execute("UPDATE favorite SET count=count+1 WHERE id=\'"+str(id)+"\'")
            db.commit()
            print('update favorite successfully')
            return "1"
        except Exception as e:
            print('update favorite failed:',e)
            db.rollback()
            return "-1"
           
if __name__=="__main__":
    app.run( host='127.0.0.1',port=8899,debug=True)
    db.close()
    print("Good bye!")