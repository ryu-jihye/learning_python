# 현재 위치에서 현재 방향을 기준으로 왼쪽 방향(반시계 방향으로 90도 회전한 방향)부터 차례대로 갈 곳 정함
# 캐릭터의 바로 왼쪽 방향에 아직 가보지 않은 칸이 존재한다면, 왼쪽 방향으로 회전만 수행하고 1단계로 돌아감
# 만약 네 방향 모두 이미 가본 칸이거나 바다로 되어 있는 칸의 경우에는, 바라보는 방햐을 유지한 채로 한 칸 뒤로 가고 1단계로 돌아간다
# 단, 이 때 뒤쪽 방향이 바다인 칸이라 뒤로 갈 수 없는 경우에는 움직임을 멈춘다

# 첫쨰 줄 맴의 세로 크기 N과 가로 크기 M을 공백으로 구분하여 입력한다. (3<=N, M<=50)
# 둘째 줄에 게임 캐릭터가 있는 칸의 좌표 (A, B)와 바라보는 방향 D가 각각 공백으로 구분하여 주어진다 방향 D의 값으로는 다음과 같이 존재한다
# 0 : 북쪽
# 1 : 동쪽
# 2 : 남쪽
# 3 : 서쪽
# 셋째 줄부터 맵이 육지인자 바다인지에 대한 정보가 주어진다 N개의 줄에 맵의 상태가 북쪽부터 남쪽 순서대로, 각 줄의 데이터는 서쪽 -> 동쪽 순서 대로 주어진다
# 맵 외곽은 항상 바다로 되어 있다
# 0 : 육지
# 1 : 바다

n, m = map(int, input().split())
d = [[0] * m for _ in range(n)] #방문한 위치를 저장하기 위한 맵을 생성하기 위해 0으로 초기화
x, y, direction = map(int, input().split()) # 현재 캐릭터의 x좌표, y좌표, 방향 입력 받기
d[x][y] = 1 # 현재 좌표 방문 처리

array = []
for i in range(n):
    array.append(list(map(int, input().split()))) #전체 맵 정보 입력 받기

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

count = 1
turn_time = 0
while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]

    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    else:
        turn_time += 1
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]

        if array[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        turn_time = 0

print(count)
