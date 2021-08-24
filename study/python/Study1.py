# 피보나치 수열

'''
def fibo(n):
    c = 1
    while True:
        c += 1
        if c > 4:
            return c

n = int(input())
answer = fibo(n)

print(answer)
'''

# 배열 공부 (list)

'''
numbers = [1,2,3,4,5]
colors = ("red","blue","green")

print (numbers)
print(colors)
numbers[0] = 100
print(numbers)
colors[0] = "Null"
print(colors)
'''

# 배열과 튜블의 차이점 (튜플 값은 수정 불가능)

'''
numbers1 = (1,2,3,4,5)
numbers2 = [6,7,8,9,10]
print(len(numbers1))
print(len(numbers2))
'''

# 걸린 시간 구하기

'''
import time

n = int(input())
a = 0
start = time.time()
for i in range (n):
    a += 1

print(a, start - time.time())
'''

# 별(*) 직각 삼각형 그리기

'''
n = int(input())
for i in range(1,n+1):
    print("*"*i,end='')
    print()
'''

# 배열 ID값 파악하기 (list ID값)


'''
list1 = [1,2,3,4,5]
list2 = list1
list2[0] = 123
list3 = list(list1)

print(list1)
print(list2)
print(list3)

print()

list1.sort()
list4 = sorted(list2)

print(list1)
print(list2)
print(list3)
print(list4)
'''

# 글로벌 변수

'''
def a ():
    global s

    print (s)
    s = "바나나"
    t = "바나나"

    print(s)
    print(t)


s = "사과"
t = "사과"
print(s)
a()
print(s)
print(t)
'''

# 함수로 배열, String 값 수정

'''
def a1 (list):
    list[0] = 123

def a2 (list,str):
    list.append(99)
    str +=  "!!!"



list1 = [1,2,3,4,5]
a = "Happy"

print(list1,a)
a1(list1)
print(list1, a)
a2(list1, a)
print (list1,a)
'''

#간단한 이중 if문

'''
math = int(input("수학 점수: "))
english = int(input("영어 점수: "))

total = math + english

if total < 110:
    print("불합격\n:총합 점수가 부족합니다.")

elif english >= 40:
        if math >= 40:
            print("합격")
        else:
            print("불합격\n:수학 점수가 부족합니다.")
else:
    print("불합격\n:영어 점수가 부족합니다.")
    '''
