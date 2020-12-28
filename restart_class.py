chicken_brands = [
    {"name": "굽네치킨", "main": "고추바사삭", "ceo": "정태용", "branch": 1234},
    {"name": "bbq", "main": "황금올리브", "ceo": "윤경주", "branch": 4567},
    {"name": "교촌치킨", "main": "교촌리얼후라이드", "ceo": "소진세", "branch": 789},
    {"name": "처갓집양념치킨", "main": "트러플슈프림양념치킨", "ceo": "신동욱", "branch": 1000}
]

print("브랜드", "주메뉴", "대표", "지점", sep="\t")

for chicken in chicken_brands:
    branch_sum = chicken["branch"]
    branch_average = branch_sum / 4

    print(chicken["name"], chicken["main"], chicken["ceo"], branch_average, sep="\t")


def create_chickens(name, main, ceo, branch):
    return {
        "name": name,
        "main": main,
        "ceo": ceo,
        "branch": branch
    }


chickens = [
    create_chickens("굽네치킨", "고추바사삭", "정태용", 1234),
    create_chickens("bbq", "황금올리브", "윤경주", 4567),
    create_chickens("교촌치킨", "교촌리얼후라이드", "소진세", 789),
    create_chickens("처갓집양념치킨", "트러플슈프림양념치킨", "신동욱", 1000)
]

print("브랜드", "주메뉴", "대표", "지점", sep="\t")
for fry in chickens:
    branch_sums = fry["branch"]
    branch_averages = branch_sums / 4

    print(fry["name"], fry["main"], fry["ceo"], branch_averages, sep="\t")
