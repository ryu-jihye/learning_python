# 실행결과
# 우리동네 제빵가게 
# 파리바게트 파운드케이크 1개
# 배스킨라빈스 아이스크림케이크 3개
# 파리크라상 쉬폰케이크 2개
# 뚜레쥬르 초코케이크 5개


cake = [
    {"brand": "파리바게트", "bread": "파운드케이크", "number": 1},
    {"brand": "배스킨라빈스", "bread": "아이스크림케이크", "number": 3},
    {"brand": "파리크라상", "bread": "쉬폰케이크", "number": 2},
    {"brand": "뚜레쥬르", "bread": "초코케이크", "number": 5}
]

print("# 우리동네 제빵가게")
for suger in cake:
    print(suger["brand"], suger["bread"], str(suger["number"]) + "개")


# 실행결과 
# {1: 3, 2: 2, 3: 3, 5: 3, 6: 2, 8: 2, 9: 2, 4: 1, 7: 1}

colors= [1, 2, 3, 5, 6, 8, 9, 1, 5, 3, 4, 2, 1, 7, 6, 9, 8, 3, 5]   
counter = {}

for red in colors:
    if red in counter:
        counter[red] = counter[red] + 1

    else:
        counter[red] = 1

print(counter)

# 실행결과 
# 이름 : 레몬
# 개수 : 20
# 색깔 : 노랑색
# 원산지 : 히말라야
# 주산지 : 칠레
# 효능 : 피부건강
# 효능 : 감기예방
# 효능 : 피로회복

fruit = {
    "이름": "레몬",
    "개수": 20,
    "색깔": "노랑색",
    "생산지": {
        "원산지": "히말라야",
        "주산지": "칠레"
    },
    "효능": ["피부건강", "감기예방", "피로회복"]
}

for lemon in fruit:
    if type(fruit[lemon]) is dict:
        for yellow in fruit[lemon]:
            print(yellow, ":", fruit[lemon][yellow])
    elif type(fruit[lemon]) is list:
        for round in fruit[lemon]:
            print(lemon, ":", round)
    else:
        print(lemon, ":", fruit[lemon])