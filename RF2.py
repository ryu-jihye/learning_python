def factorial_iterative(n):
    result = 1 # 1부터 n까지의 수를 차례대로 곱하기
    for i in range(i, n+1):
        result *= i
    return result

def factorial_recursive(n): # 재귀적으로 구현한 n!
    if n <= 1:
        return 1 
    return n * factorial_recursive(n-1) #1 이하인 경우 1로 반환 * n! = n * (n-1)!

print("반복적으로 구현:", factorial_iterative(5))
print("재귀적으로 구현:", factorial_recursive(5))
