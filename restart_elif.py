# 실행결과
# 태어난 월을 입력해주세요 > 1
# 물병자리 입니다


str_input = input("태어난 월을 입력해 주세요>")
birth_start_month = int(str_input) % 12

if birth_start_month == 3:
    print("양자리입니다")
elif birth_start_month == 4:
    print("황소자리입니다")
elif birth_start_month == 5:
    print("쌍둥이자리입니다")
elif birth_start_month == 6:
    print("게자리입니다")
elif birth_start_month == 7:
    print("사자자리입니다")
elif birth_start_month == 8:
    print("처녀자리입니다")
elif birth_start_month == 9:
    print("천칭자리입니다")
elif birth_start_month == 10:
    print("전갈자리입니다")
elif birth_start_month ==11:
    print("궁수자리입니다")
elif birth_start_month == 12:
    print("염소자리입니다")
elif birth_start_month == 1:
    print("물병자리입니다")
elif birth_start_month == 2:
    print("물고기자리입니다")