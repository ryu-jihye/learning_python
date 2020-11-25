students = [
    학생_생성("윤인성", 87, 98, 88, 95),
    학생_생성("연하진", 92, 98, 96, 98),
    학생_생성("구지연", 76, 96, 94, 90),
    학생_생성("나선주", 98, 92, 96, 92),
    학생_생성("윤아린", 95, 98, 98, 98),
    학생_생성("윤명월", 64, 88, 92, 92)
]

def 학생_생성(name, korean, math, english, science):
    return {
        "name": name,
        "korean": korean,
        "math": math,
        "english": english,
        "science": science
    }

def 총점(student):
    return student["korean"] + student["math"] +\
        student["english"] + student["science"]
def 평균(student):
    return 총점(student) / 4
def 출력(student):
    print(student["name"], 총점(student), 평균(student), sep="\t")

print("이름", "총점", "평균", sep="\t")
for student in students:
    출력(student)