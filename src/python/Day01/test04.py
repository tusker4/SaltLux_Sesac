import pickle

for i in range(1,6):
    with open (f"{i}주차보고", "w", encoding="utf8") as s:
        s.write(f"-{i}번째 보고- \n 부서 : \n 이름 : \n 업무 요약 :")