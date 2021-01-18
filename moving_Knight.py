# 나이트 이동방법
# 수평으로 두 칸 이동한 뒤에 수직으로 한 칸 이동하기
# 수직으로 두 칸 이동한 뒤에 수평으로 한 칸 이동하기

# 첫째 줄에 8*8 좌표 평면상에서 현재 나이트가 위치한 곳의 좌표를 나타내는
# 두 문자로 구성된 문자열이 입력된다 입력문자는 a1처럼 열과 행으로 이루어진다
# 첫째 줄에 나이트가 이동할 수 있는 경우의 수는?

# 나이트의 이동경로(규칙 적용)
# steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1

steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

result = 0
for step in steps:
    next_row = row + step[0]
    next_column = column + step[1]

    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        result += 1

print(result)