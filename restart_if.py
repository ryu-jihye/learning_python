# 실행결과
# 1번째 숫자 : 2920
# 2번째 숫자 : 2014

# 처음 입력했던 2020가 2014보다 큽니다

a = float(input("> 1번째 숫자: "))
b = float(input("> 2번째 숫자: "))
print()

if a > b:
    print("처음 입력했던 {}가 {}보다 더 큽니다".format(a, b))
else:
    print("두 번째로 입력했던 {}가 {}보다 더 큽니다".format(b, a))