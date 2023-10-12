
from flask import Flask


# step2. 
app = Flask(__name__)
print(__name__)

# step3.
@app.route('/')
def home():
    return '홈화면이야'


# step4. 
if __name__ == '__main__':
    app.run(debug=True)
    # debug=True : 수정 -> 저장 -> 자동리로드


