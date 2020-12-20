list_number = [9, 50, 83, 22, 76, 95]

try:
    number_input = int(input("정수 입력>"))
    print("{}번째 요소: {}".format(number_input, list_number[number_input]))
except Exception as exception:
    print("type(exception):", type(exception))
    print("exception:", exception)

# list 이외의 값 입력 : type(exception): <class 'IndexError'> exception: list index out of range(범위 내x)
# 숫자(int)대신 문자 입력 : type(exception): <class 'ValueError'> exception: invalid literal for int() with base 10: 'merry xmas'

# try:
#   예외가 발생할 가능성이 있는 구문
# except 예외의 종류 A:
#   예외A가 발생했을 때 실행할 구문
# except 예외의 종류 B:
#   예외B가 발생했을 때 실행할 구문
# except 예외의 종류 C:
#   예외C가 발생했을 때 실행할 구문

list_number_A= [9, 50, 83, 22, 76, 95]

try:
    number_input_A = int(input("정수 입력2>"))
    print("{}번째 요소: {}".format(number_input_A, list_number_A[number_input_A]))
except ValueError:
    print("정수를 입력해 주세요!") #정수 이외의 값 입력 시 문구가 나옴
except IndexError:
    print("리스트 인덱스를 벗어났어요!") # 리스트 값 이외의 값 입력 시 문구가 나옴