def process(a,b):
    money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    total = b-a
    if total >= 0:
        print("거스름 돈 : {}원".format(total))
        total2 = total % 10
        if total2 != 0:
            print("10원 미만은 거슬러 드릴 수 없습니다.")
        else:
            for i in range(len(money)):
                if total - money[i] >= 0:
                    print("{}원 {}장".format(money[i], total // money[i]), end=' ')
                    total -= money[i] * (total // money[i])
    else:
        print("{}원 부족합니다.".format(a-b))

price = int(input("물건의 가격을 입력하십시오 : "))
money = int(input("지불하실 돈을 입력하십시오 : "))

process(price, money)

