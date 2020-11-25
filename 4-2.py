# 리스트 = []
# 리스트 = [1, 2, 3]
#리스트[0]

딕셔너리 = {
   "문자열" : "값A",
   273 : "값B",
   True : False
}

print(딕셔너리["문자열"])
print(딕셔너리[273])
print(딕셔너리[True])

딕셔너리["문자열"] = "값값"
print(딕셔너리["문자열"])

for key in 딕셔너리:
    print("{} : {}".format(key, 딕셔너리[key]))

del 딕셔너리["키"]
print()
for key in 딕셔너리:
    print("{} : {}".format(key, 딕셔너리[key]))
