# Syntax Error =/= Exception
# Synatx Error : 프로그램이 실행되기 전에 발생하는 오류, 해결하지 않으면 프로그램 자체가 실행 불가
# Exception : 프로그램 실행 중에 발생되는 오류, 프로그램 실행 후 해당 지점에서 오류 발생

# 실행결과
# (1) 요소 내부에 있는 값 찾기
# 38은 0 위치에 있습니다

# (2) 요소 내부에 없는 값 찾기
# 리스트 내부에 없는 값입니다

# --- 정상적으로 종료되었습니다. --- 

numbers = [38, 52, 93, 22, 87, 10, 200]

print("(1) 요소 내부에 있는 값 찾기")
print(" {}는 {} 위치에 있습니다".format(38, numbers.index(38)))

print("(2) 요소 내부에 없는 값 찾기")
number = 999
if number in numbers: # 다른 표현 : try:
        print(" {}는 {} 위치에 있습니다".format(38, numbers.index(38)))
else: # 다른 표현 : elif number not in numbers:
        print("리스트 내부에 없는 값입니다")
print()

print("--- 정상적으로 종료되었습니다. ---")

# output = 20 + "수" → 예외(ValueError)
# int("크리스마스") → 예외(ValueError)
# cursor.close) → 구문 오류(SyntaxError)
# [5, 4, 3, 2, 1][9] → 예외(IndexError)