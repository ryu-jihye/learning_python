# 첫 번쨰 줄에 얼음 틀의 세로 길이 N과 가로 길이 M이 주어진다(1<=N, M<=1000)
# 두 번째 줄부터 N+1 번째 줄까지 얼음 틀의 형태가 주어진다
# 이 때 구멍이 뚫려있는 부분은 0, 그렇지 않은 부분은 1DLEK

# 한 번에 만들 수 있는 아이스크림의 개수를 출력한다

n, m = map(int, input().split*())

graph = []
for i in range(i):
    graph.append(list(map(int, input())))

def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    if graph[x][y] == 0:
        graph[x][y] =1
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1

print(result)