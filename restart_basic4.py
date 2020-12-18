# 실행결과
# 1::2::3::4::5::6

numbers =[1, 2, 3, 4, 5, 6]

print("::".join(map(str, numbers))) #map() must have at least two arguments.(map은 적어도 2개이상 사용해야 함)
# map(함수, 리스트) : 리스트의 요소를 함수에 넣고 리턴된 값으로 새로운 리스트 구성

print(str(numbers)) 
# 결과 : [1, 2, 3, 4, 5, 6]
# str(): 숫자를 문자열로 변환
print(str, numbers)
# 결과 : <class 'str'> [1, 2, 3, 4, 5, 6]

# 실행결과
# 홀수만 추출하기
# [1, 3, 5, 7, 9]

# 3 이상, 7 미만 추출하기
# [3, 4, 5, 6]

# 제곱해서 50미만 추출하기
# [1, 2, 3, 4, 5, 6, 7]

anumbers = list(range(1, 10+1))

print("# 홀수만 추출하기")
print(list(filter(lambda x: x % 2 == 1, anumbers)))

print("# 3 이상, 7 미만 추출하기")
print(list(filter(lambda x: 3 <= x < 7, anumbers)))

print("#제곱해서 50미만 추출하기")
print(list(filter(lambda x: x ** 2 < 50, anumbers)))

# lambda : 간단한 함수를 쉽게 선언하는 방법
# lambda 매개변수(위에서는 x) : 리턴값(=조건)