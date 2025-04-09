from flask import Flask,request,jsonify,session
from werkzeug.utils import redirect

app=Flask(__name__)
app.secret_key='hello'

@app.route("/", methods=["GET"])
def hello_world():
    return "hello,python "


# 登录
@app.route('/user/login',methods=['POST'])
def login():
    data=request.get_json()
    username=data.get('username')
    password=data.get('password')

    if not all([username,password]):
        return jsonify(code=1,msg='参数不完整')


    if username=='admin' and password=='123456':
        session['username']=username
        return jsonify(code=0,msg='登录成功')
    else:
        return jsonify(code=2,msg='用户名或密码错误')

        
app.run(host="127.0.0.1")