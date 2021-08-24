import math

def calcPPP(c):
    a = math.pi * c * c
    b = 2 * math.pi * c
    return (a, b)



x, y = calcPPP(3)
print(x, y)

# 내장 함수 사용 연습
'''
a1 = [2,4,6,8,10]
a2 = [1,3,5,7]
a3 = [8,9,10]

new1 = list(zip(a1, a2))
print(new1)

for i, v in enumerate (a1):
    print(i, v)

people = {'김철수' : 35, '용수철' : 30, '국민대' : 24}

for key, value in people.items():
    print(key, value)

print(sum(new1[0]))
'''


# 선형탐색
'''
import random

def process(target):
    low = 0
    upper = len(numbers) - 1
    idx = -1
    while (low <= upper):
        middle = int((low + upper) // 2)
        if numbers[middle] == target:
            idx = middle
            break
        elif numbers[middle] > target:
            upper = middle - 1
        elif numbers[middle] < target:
             low = middle + 1
    if idx == -1:
        print("{}을 찾지 못했습니다.".format(target))
    else:
        print("{}을 찾았습니다!".format(target))

number = int(input("랜덤값으로 만들 값의 갯수를 입력하세요 : "))
target = int(input("검색값을 입력하세요 : "))

numbers = [random.randint(0, number) for x in range(number)]

print(numbers)
process(target)
'''

# 그냥 탐색..
'''
if target in numbers:
    print("존재합니다")
else:
    print("존재하지 않습니다.")
'''