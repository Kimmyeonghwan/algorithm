def process(m, kg):
    BMI = kg / pow(m, 2)
    print("입력하신 키와 몸무게의 BMI는 {} 입니다.".format(BMI), end = '\n')

    if BMI <= 18.5:
        print("저체중 입니다.")

    elif (BMI > 18.5 and BMI < 23):
        print("정상 체중 입니다.")

    elif (BMI >= 23 and BMI < 24.9):
        print("과체중 입니다.")

    elif BMI >= 25:
        print("비만 입니다.")

userCm, userKg = input("키와 몸무게를 입력해주세요.: ").split()
userCm = float(userCm)
userM = userCm * 0.01
userKg = float(userKg)

process(userM, userKg)