try:

    number_intput_a = int(input("정수입력> "))
    print("원의 반지름:", number_intput_a)
    print("원의 둘레:", 2 * 31.4 * number_intput_a)
    print("원의 넓이:", 3.14 * number_intput_a * number_intput_a)
except Exception as exception:
    print("type(exception):", type(exception))
    print("exception:", exception)
