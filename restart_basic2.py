# 실행결과
#원본 = [4, 7, 9, [1, [5]], [6, 8, 3]]
#변환 = [4, 7, 9, 1, 5, 6, 8, 3]

def flatten(data):

    output = [] #출력을 리스트 속에 할 것
    for item in data: #주어진 data 속에 item있는지 확인
        if type(item) == list: # 만약 item이 list라면 2차원 리스트 1차원으로
            output += flatten(item)
        else:
            output.append(item) # 리스트가 아닐 경우 리스트에 값을 더함
    return output

example = [4, 7, 9, [1, [5]], [6, 8, 3]] #원본 데이터는 리스트 안에 또 다른 리스트도 있으나 처음 리스트 속 숫자도 존재
print("원본:", example)
print("변환:", flatten(example))