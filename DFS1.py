INF = 9999999999999999999

graph = [
    [0, 7, 5],
    [7, 0, INF],
    [5, INF, 0]
]

print(graph)

graph2 = [[] for _ in range(3)] #행이 3개인 2차원 리스트로 인접 리스트 표현

graph2[0].append((1,7))
graph2[0].append((2, 5))

graph2[1].append((0, 7))

graph2[2].append((0, 5))

print(graph2)
