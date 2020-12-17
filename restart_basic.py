
# f(x) = 2x + 1
def f(x):
    return 2 * x + 1
print(f(10))

# p(x) = x^2 + 2x + 1

def p(y):
    return y ** 2 + 2 * y + 1 # 다른 표현 : y * y + 2 * y + 1
print(p(10))


# 실행결과
# 3150

def mul(*values):
    output = 1
    for value in values:
        output *= value
    return output
print(mul(5, 7, 9, 10))

# 틀린 오답
#for i in range(): → output처럼 숫자로 범위 지정
#        for value in values:
#            print(value) → output을 통해 value의 계산식 설정
#    print() → return output을 통해 가변 매개변수 설정


# 정상 호출
def function(valueA=10, valueB=20, *values):
    pass
function(1, 2, 3, 4, 5)

# 정상 호출
def function(valueA, valueB, *values):
    pass
function(1, 2, 3, 4, 5)

# 정상 호출
def function(*values, valueA=10, valueB=20):
    pass
function(1, 2, 3, 4, 5)

# 문제 발생
def function(*values, valueA, valueB): # 순서가 바뀔 경우 valueA, B에 값 지정 필요 
    pass
function(1, 2, 3, 4, 5)