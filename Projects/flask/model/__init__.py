# 모델을 의미,
# 모델 서빙, 예측 처리 기능 제공
import joblib
# 모델, 레이블 로드 처리 (전역처리)
import os
import re
from string import ascii_lowercase

print(os.path.abspath(__file__))
print(os.path.realpath(__file__))
# 경로 만들기 (개발 : 윈도우, 서비스: 리눅스)
print(os.path.join(os.path.dirname(__file__) , 'lang_predict.ml'))

# 1. 모델로드
model = joblib.load(os.path.join(os.path.dirname(__file__) , 'lang_predict.ml'))

# 2. 레이블로드
label = joblib.load(os.path.join(os.path.dirname(__file__) , 'lang_predict.lb'))

# 3. 번역요청 원본 데이터 -> 학습용 전처리 함수
# 텍스트 => 일련의 과정(전처리) => (1, 26), 2차원 리스트
# 텍스트라서 src
def encode_freqs_data(src : str = 'train') -> list:
    '''
    - 텍스트 원문 -> 빈도계산 및 정답추출하려 특정구조로 리턴
    - parameters
      - src : 번역 요청 원문 텍스트
    - returns
      - list : [[0.001, ......]]
    '''
    ALPHA_LEN = len(ascii_lowercase)  # 1회만 작동
    STD_ASCII_A = ord('a')
        # 정답 데이터  
    text = src.lower()
    p    = re.compile('[^a-z]*')
    text = p.sub('', text)
    counts = [0] * ALPHA_LEN    
    for ch in text:
        counts[ord(ch)-STD_ASCII_A] += 1
    total_count = len(text)
    counts_norms = list(map(lambda x: x/total_count , counts))
    print('# 3. 번역요청 원본 데이터 ', [counts_norms])
    return [counts_norms]

   
# 4. 예측 수행 함수
def predict( data:list ) -> dict:
    # 4-1. 모델 예측 수행
    pred_y = model.predict(data)
    print("#4. 예측수행함수 : ", pred_y)
    return { 
               "success" : 1,
               "code"    :pred_y[0],
               "ko"      :label[pred_y[0]]
               }
    
# x.py 를 직접 수행 : __name__ => '__main__'
# x.py 를 다른 py가 모듈 가져오기 : __name__ => 'X'

if __name__ == '__main__':
    # 단위 테스트 용도
    sample_data = '''
                             American football (referred to simply
                             as football in the United States and Canada),
                             also known as gridiron,[nb 1] is a team sport
                             played by two teams of eleven players on a rectangular field
                             with goalposts at each end. The offense,
                             the team with possession of the oval-shaped football,
                             attempts to advance down the field by running with the ball 
                             or passing it, while the defense, 
                             the team without possession of the ball, 
                             aims to stop the offense's advance and to take control of the ball
                             for themselves. The offense must advance 
                             at least ten yards in four downs or plays;
                             if they fail, they turn over the football to the defense,
                             but if they succeed,
                             they are given a new set of four downs to continue the drive.
                             Points are scored primarily by advancing the ball 
                             into the opposing team's end zone 
                             for a touchdown or kicking the ball 
                             through the opponent's goalposts for a field goal.
                             The team with the most points at the end of a game wins.
                             '''
    # 데이터 전처리
    preprocessing_data = encode_freqs_data(sample_data)
    # 예측
    result = predict(preprocessing_data)
    print(result)
    
    # 4-2.응답데이터 구성
    