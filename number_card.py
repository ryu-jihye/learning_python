# 첫째 줄에 숫자 카드들이 놓인 행의 개수 n과 열의 개수 m이 공백을 기준으로 하여 각각 자연수로 주어진다(1<=n, m<=100)
# 둘째 줄부터 n개의 줄에 걸쳐 각 카드에 적힌 숫자가 주어진다 각 숫자는 1이상 10000이하의 자연수이다
# 출력 조건 : 첫째 줄에 게임의 룰에 맞게 선택한 카드에 적힌 숫자를 출력한다
# 힌트 : 각 행마다 가장 작은 수를 찾은 뒤에 그 수 중에서 가장 큰 수를 찾는 것


n, m = map(int, input().split())

result = 0

for i in range(n):
    data = list(map(int, input().split()))
    min_value = min(data)

    result = max(result, min_value)

print(result)