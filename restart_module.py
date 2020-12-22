# from 모듈 이름 import 가져오고 싶은 변수 또는 함수
# import 모듈 as 사용하고 싶은 식별자

import random
print("random module") 

print("-random():", random.random()) # random() : 0 ~ 1 사이의 float값 리턴

print("-uniform(10, 20):", random.uniform(10, 20)) # uniform() : 지정한 범위 내에서 float값 리턴

print("-randrange(10):", random.randrange(10))
print("-randrange(2, 5):", random.randrange(2, 5)) 
# randrange() : 지정한 범위 내에서 int()값 리턴
# randrange(max) : 0 ~ max 사이 int값 리턴
# randerange(min, max) : min ~ max 사이 int값 리턴

print("-choice([1, 2, 3, 4, 5]):", random.choice([1, 2, 3, 4, 5])) # choice(list) : 리스트 내부에 있는 요소를 랜덤 선택

print("-shuffle([1, 2, 3, 4, 5]):", random.shuffle([1, 2, 3, 4, 5])) # shuffle(list) : 리스트 요소 랜덤하게 섞음

print("-sample([1, 2, 3, 4, 5,]):", random.sample([1, 2, 3, 4, 5], k=2)) # sample(list, k=숫자) : 리스트 요소 중에 k개 뽑음


import sys

print(sys.argv) #명령 매개변수 출력 : ['restart_module.py']

print("getwindowsversion:()", sys.getwindowsversion())
print("copyright:", sys.copyright)
print("version:", sys.version)

sys.exit()