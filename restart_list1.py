# 실행결과
# 100 이상의 수 : 150
# 100 이상의 수 : 200
# 100 이상의 수 : 300

numbers= [73, 150, 200, 70, 23, 300, 45, 99]

for number in numbers:
    if number >= 100:
        print("-100 이상의 수:", number)

# 실행결과
# 73은 2 자리수입니다
# 150은 3 자리수입니다
# 200은 3 자리수입니다
# 7은 1 자리수입니다
# 23은 2 자리수입니다
# 300은 3 자리수입니다
# 45은 2 자리수 입니다
# 99는 2 자리수입니다.

green= [73, 150, 200, 70, 23, 300, 45, 99]

for abocado in green:
    print(abocado, "는", len(str(abocado)), "자리수입니다")

# 문자의 길이 len(str(값))

# 실행결과
# 73은 홀수입니다
# 150은 짝수입니다
# 200은 짝수입니다
# 7은 홀수입니다
# 23은 홀수입니다
# 300은 짝수입니다
# 45은 홀수입니다
# 99는 홀수입니다

green= [73, 150, 200, 70, 23, 300, 45, 99]

for cucumber in green:
    if cucumber % 2 == 1:
        print(cucumber, "은 홀수입니다")
    else:
        print(cucumber, "은 짝수입니다")

    
# 실행결과 
1
2
3
4
5
6
7
8
9

list_of_list = [
    [1, 2, 3],
    [4, 5, 6, 7],
    [8, 9]
]

for i in list_of_list:
   for e in i:
       print(e)


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
output = [[], [], []]

for number in numbers:
    output[(number + 2) % 3].append(number) #output[(number + 3) % 2].append(number)-> [[1, 3, 5, 7, 9], [2, 4, 6, 8], []]

print(output)