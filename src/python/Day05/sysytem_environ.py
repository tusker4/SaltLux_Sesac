import re
import os.path

ip_pattern = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
ip_counter = {}
logFile = os.path.join('.', 'access.log.2017-10-13')
logData = None
with open(logFile, 'r') as fp:
    logData = fp.read()
ips = re.findall(ip_pattern, logData)
for ip in ips:
    if ip in ip_counter:
        ip_counter[ip] += 1
    else:
        ip_counter[ip] = 1

for key, value in ip_counter.items():
    print(f"{key} : {value}")


# reverse=True) 내림차순
sorted_counter = sorted(ip_counter, key=lambda x: x[1], reverse=True)[:10]
print("sorted_counter  : ", sorted_counter)

# savefile = os.path.join('.', 'statics.txt')
# with open(savefile, 'w') as fp:
#     for value in sorted_counter:
#         # iterable 타입을 받는다 -> list 는 iterable타입이라 O
#         fp.write(f"{key} :{value}\n")
# print(f"통계 자료를 {savefile} 파일로 저장하였습니다.")
