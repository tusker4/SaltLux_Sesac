# step1 모듈 가져오기
from flask import Flask
# 첫글자가 대문자니까 클래스이다. (Flask)

# step2. 플라스크 객체 생성
app = Flask(__name__)
# step3. 특정 주소를 요청 -> 해석 -> 누가처리할지 지정 -> 서버가 응답 => 라우팅
@app.route('/')
def home():
    return '환영합니다.'

# step4. 서버가동
if __name__ == '__main__': # 직접 실행한다면
# debug=True : 수정 -> 저장 -> 자동리로드
    app.run(debug=True)

