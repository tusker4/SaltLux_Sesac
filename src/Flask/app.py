
from flask import Flask, render_template, request
from os.path import join
from os import listdir


app = Flask(__name__, static_folder='./resources/', static_url_path='/')


@app.route('/')
def index():
    return "안녕하세요. 플섭aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"


@app.route('/joinin')
def joinin():
    return "여기는 조인 페이지입니다.dddddddddddddddddddddddddd" 


@app.route('/signup')
def singup():
    data = 'abcd'
    return "여기는 사인업 페이지입ㄴ니닫"

@app.route('/email')
def email():
    email = request.args.get('email', 'Unknown')
    name = request.args.get()
    return "여기는 기타페이지"


if __name__ == '__main__':
    app.run(host='0,0,0,0', port=80, debug=True)
