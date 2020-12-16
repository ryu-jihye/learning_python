# 실행 결과
# 2 : 10
# 5 : 101
# 6 : 110
# 11 : 1011
#...
# 62 : 111110
# 95 : 1011111
# 합계 : 539

# 1번 케이스 풀이법(리스트 내포)
output = [i for i in range(1, 100+1)
    if "{:b}".format(i).count("0") == 1]

for i in output:
    print("{} : {}".format(i, "{:b}".format(i)))
print("합계:", sum(output))


# 2번 케이스 풀이법

output = 0

for i in range(1, 100 + 1):
    if "{:b}".format(i).count("0") == 1:
        print("{} : {:b}".format(i, i))
        output += 1
print("합계 : {}".format(output))


# 1 ~ 100 / 2진수 / 0이 포함된 숫자 > 합
#for i in range(1, 100 + 1):
#   print("{:b}".format(i)) # 2진수 만드는 법
#   if "{:b}".format(i).count("0") == 1
#   print("{:b}".format(i)) # 2진수 / 0이 포함된 숫자 > 합