try:
    a = [273, 103, 52, 57, 100]
    number = int(input("정수 입력(0~4까지 입력해주세요)>"))
    print(a[number])
except Exception as exception:
    if type(exception) == ValueError:
        print("값에 문제가 있습니다.")
    elif type(excpetion) == IndexError:
        print("0~4까지를 입력해주세요.")