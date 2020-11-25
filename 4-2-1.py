dictionary = {
    "이름" : "구름", 
    "종족" : "강아지"   
}

print(dictionary.get("이름"))
print(dictionary["이름"])

if dictionary.get("나이") == None:
    dictionary.get("나이")
else:
    print("없는 키입니다")


pets = [
    {"name": "구름", "age": 5},
    {"name": "초코", "age": 3},
    {"name": "아지", "age": 1},
    {"name": "호랑이", "age": 1},
]

print("# 우리 동네 애완 동물들")

for pet in pets:
    print("{} {}살".format(pet["name"], pet["age"]))


numbers = [1,2,6,8,4,3,2,1,9,5,4,9,7,2,1,3,5,4,8,9,7,2,3]
counter = {}

for number in numbers:
    if number in counter:
        counter[number] += 1
    else:
        counter[number] = 1
    
print(counter)

character = {
    "name": "기사",
    "level": 12,
    "items": {
        "sword": "불꽃의 검",
        "armor": "풀플레이트"
    },
    "skill": ["베기", "세게 베기", "아주 세게 베기"]
}

for key in character:
    if type(character[key]) is dict:
        for k in character[key]:
            print("{} : {}".format(k, character[key][k]))
    elif type(character[key]) is list:
            for item in character[key]:
                print("{} : {}".format(key, item))
    else:
            print("{} : {}".format(key, character[key]))
