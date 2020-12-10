print(__name__)
# 엔트리 포인트 내부에서 __name__은 "__main__"이라는 문자열

import module_name

print(module_name.americano)
print(module_name.latte)
print(module_name.cocoa)

if __name__ == "__cost__":
    print("음료 값입니다A")