# html 을 읽어서 랜더링(필요시 데이터를 넣어서 동적구성)후 응답 -> SSR 

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/detect_lang', method =['POST'])
def detect_lang():
    ori_text =request.form.get('text')
    
    return f'받은 텍스트는 {ori_text}'

@app.route('/ssgo', methods=['GET', 'POST'])
def ssgo():
    if request.method == 'GET':
        return render_template('index2.html')
    else:
        ori_text = request.args.get('ori_text')
        print(ori_text)
        res ={
            "success" : 1,
               "code":'en',
               "ko":"영어"
        }
        return jsonify(res)
    

if __name__ == '__main__':
    app.run(debug=True)
