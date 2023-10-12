import joblib
import os
import re



#1. 모델로드, 라벨로드
# joblib.load(os.path.join())
# init.py 의주소
model = joblib.load(os.path.join(os.path.dirname(__file__), 'lang_predict.ml'))
label = joblib.load(os.path.join(os.path.dirname(__file__), 'lang_predict.lb'))
# 3. 원본데이터
# 데이터 전처리 
def encode_freqs_data(src : str = 'train') -> list:
    text = src.lower()
    p = re.compile('[^a-z]*')
    text = p.sub('', text)
    counts = [0] * 26
    for ch in text:
        counts[ord(ch) - 97] += 1
        print('ch : ', ch)
    total_count = len(text)
    counts_norms = list(map(lambda x: x/total_count, counts))    
    return [counts_norms]
# 4. 예측 수행함수
def predict(data:list)-> dict:
    pred_y = model.predict(data)
    
    return { 
               "success" : 1,
               "code"    :pred_y[0],
               "ko"      :label[pred_y[0]]
               }
    
if __name__ == '__main__':
    sample_data = ''' American football (referred to simply
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
                             The team with the most points at the end of a game wins. '''
    processing_data = encode_freqs_data(sample_data)
    result = predict(processing_data)
    print(result)