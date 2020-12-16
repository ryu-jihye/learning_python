# 실행결과
# {'name': '제주', '관광지': 한라산, '음식': 한라봉, '방문 월': 12}

tour_list = ["name", "관광지", "음식", "방문월"]
value_list = ["제주", "한라산", "한라봉", 12]
character = {}


for t in range(0, len(tour_list)):
    character[tour_list[t]] = value_list[t]
    #문자형식 -> 숫자형식(name : 0번째 자리, 관광지 : 1번째 자리, 음식 : 2번째 자리, 방문월 : 3번째 자리 ∴ len(key_list) = 0~3)
    # tour_list와 마찬가지로 value_list도 자리수로 숫자 표시
print(character)


# 실행결과
# 142를 더할 때 10000을 넘으며 그때의 값은 10011입니다

limit = 200
i = 50

sum_value = 0
while sum_value < limit: #sum_value가 limit보다 작을 경우 i를 계속 더함 
    sum_value += i
    i += 5

print("{}를 더할 때 {}을 넘으며 그 때의 값은 {}입니다.".format(i, limit, sum_value))


# 실행결과
# 1 * 99, 2 * 98, 3 * 97, ..., 98 * 2, 99* 1
# 최대가 되는 경우 50 * 50 = 2500

max_value = 0
a = 0
b = 0

for i in range(1, 100 // 2 + 1):
    j = 100 - i

    case = i * j
    if case > max_value: # case < max_value = 0 * 0 = 0이 나옴
        a = i
        b = j
        max_value = case


print("최대가 되는 경우: {} * {} = {}".format(a, b, max_value))