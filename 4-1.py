list_a = [1, 2, 3]
list_b = [4, 5, 6]

print("# 리스트")
print("list_a =", list_a)
print("list_b =", list_b)
print()

# 기본연산자
print("#리스트 기본 연산자")
print("list_a + list_b =", list_a + list_b)
print("list_a * 3", list_a * 3)
print()

#함수
print("#길이 구하기")
print("len(list_a) =", len(list_a))

#리스트를 선언합니다.
list_a = [1, 2, 3]

print("#리스트 뒤에 요소 추가하기")
list_a.append(4)
list_a.append(5)
print(list_a)
print()

#리스트 중간에 요소 추가하기
print("#리스트 중간에 요소 추가하기")
list_a.insert(0, 10)
print(list_a)

#extend
list_a = [1, 2, 3]
list_a.extend([4, 5, 6])
print(list_a)

#del, pop

list_a = [0, 1, 2, 3, 4, 5]
print("# 리스트의 요소 하나 제거하기")

#제거 방법[1] - del
del list_a[1]
print("del list_a[1]:", list_a)

#제거 방법[2] - pop
list_a.pop(2)
print("pop(2):", list_a)

#제거 방법[2] - del
list_b = [0, 1, 2, 3, 4, 5, 6]
del list_b[3:6]
print("del list_b[3:6]:", list_b)

#제거 방법[3] - del
list_c = [0, 1, 2, 3, 4, 5, 6]
del list_c[:3]
print("del list_c[:3]:, list_c)

del list_c[3:]
print("del list_c[3:]:, list_c")

#리스트 제거 - remove
list_c = [1, 2, 1, 2]
list_c.remove(2)
list_c

# 리스트 제거 - clear
list_d = [0, 1, 2, 3, 4, 5]
list_d.clear()
list_d


# for 반복자 in 반복할 수 있는 것:
 # 코드

 #리스트를 선언합니다.
 array = [273, 32, 103, 57, 52]

 for element in array:
#출력합니다.
    print(element)

# for 반복열과 문자열
for character in "안녕하세요":
    print("-", character)

# 마무리 p.157
list_a = [0, 1, 2, 3, 4, 5, 6, 7]
list_a.extend(list_a)
list_a.append(10)
list_a.insert(3, 0)
list_a.remove(3)
list_a.pop(3)
list_a.clear()

# 마무리 p.158
numbers = [273, 103, 5, 32, 65, 9, 72, 800, 99]
for number in numbers:
    if number >= 100:
        print("- 100 이상의 수:", number)


# 마무리 p.158 3번-1
numbers = [273, 103, 5, 32, 65, 9, 72, 800, 99]
for number in numbers:
    if number % 2 == 1:
        print(number, "는 홀수입니다.")
    else #number % 2 == 0:
        print(number, "는 짝수입니다.")

# 마무리 p.158 3번-2
numbers = [273, 103, 5, 32, 65, 9, 72, 800, 99]
for number in numbers:
    print(number, "는", len(str(number)), "자릿수입니다.")


# 마무리 p.159 4번
list_of_list = [
    [1, 2, 3],
    [4, 5, 6, 7],
    [8, 9]
]

for line in list_of_list:
    for itemn in line:
        print(item)
    

# 마무리 p.159 5번
numbers  = [1, 2, 3, 4, 5, 6, 7, 8, 9]
output = [[], [], []]

for number in numbers:
    output[(number + 2) % 3].append(number)

print(output)