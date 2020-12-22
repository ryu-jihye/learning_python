import os

print("현재 운영체제:", os.name)
print("현재 폴더:", os.getcwd())
print("현재 폴더 내부의 요소:", os.listdir())

os.mkdir("hello") #폴더 만들기
os.rmdir("hello") #폴더 제거하기

with open("original.txt", "w") as file: #파일 생성
    file.write("hello") 
os.rename("original.txt", "new.txt") #파일 이름명 바꿈

os.remove("new.txt") #파일 삭제하기

os.system("dir") #시스템 명령어 실행 # 파일들의 개수, 몇 바이트를 구성하는 지, 몇 바이트가 남는지 확인

import datetime

now = datetime.datetime.now() # 현재 시간

print("#datetime.timedelta로 시간 더하기")
after = now + datetime.timedelta(\
    weeks=1,\
    days=1,\
    hours=1,\
    minutes=1,\
    seconds=1)

print(after.strftime("%Y{} %M{} %D{} %H{} %M{} %S{}").format(*"년월일시분초")) #출력값 2020년 15월 12/31/20일 00시 15분 08초
print()

print("#now.replace()로 1년 더하기")
output = now.replace(year=(now.year + 1))
print(output.strftime("%Y{} %M{} %D{} %H{} %M{} %S{}").format(*"년월일시분초")) #출력값 2021년 14월 12/22/21일 23시 14분 07초