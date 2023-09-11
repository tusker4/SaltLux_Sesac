import glob
import os
from datetime import datetime
import time

print(datetime.now())
print(datetime.strftime("%Y-%m-%d"))

print(os.getcwd())

print(glob.glob("*.py"))

folder = "sample_dir"
if os.path.exists(folder):
    print("파일이 존재합니다.")
    os.rmdir(folder)
    print("폴더를 삭제했습니다.")
else:
    os.makedirs(folder)
    print(folder, "폴더를 생성했습니다.")
