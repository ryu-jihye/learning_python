# 처음 연산 : N에서 1을 뺀다
# 다음 연산 : N을 K로 나눈다

# N과 K가 주어질 때 N이 1이 될 때까지 1번 혹은 2번의 과정을 수행해야 하는 최소 횟수를 구하는 경우는?
# N(2<=N<=100,000), K(2<=K<=100,000)가 공백으로 구분되며 각각 자연수로 주어진다 
# N은 항상 K보다 크거나 같다
# 첫 째줄에 N이 1이 될 때까지 1번 혹은 2번의 과정을 수행해야 하는 횟수의 최소값은?

# 힌트 : 최대한 많이 나누기

n, k = map(int, input().split())
result = 0

while True:
    target = (n // k) * k
    result += (n - target)
    n = target

    if n < k:
        break
    result += 1
    n //= k

result += (n-1)
print(result)