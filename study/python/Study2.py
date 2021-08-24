#별그리기
'''
a = int(input("Enter a number: "))
for i in range (1,a+1):
    print("*"*i)
'''

#사전
'''
wordcount = {'dog':3,'cat':5,'tiger':3}
print(wordcount['dog'])
wordcount['dog'] += 1
word = input("Word : ")
print( wordcount[word])

for k in wordcount.keys():
    print(k)

for j in wordcount.values():
    print(j)

for z in wordcount.items():
    print(z)
'''

#최대 최솟값 구하기
''' 
data = input("Enter list of numbers: ")
numbers = data.split()
numbers = [int(i) for i in numbers]
minval = numbers[0]
minidx = 0
for i in range(1,len(numbers)):
    if (minval > numbers[i]):
        minval = numbers[i]
        minidx = i
print(minval, minidx)
'''

#피보나치 (재귀함수의 대표적)
'''
def fibo(n):
    if (0 <= n <= 1):
        return n
    else:
        return fibo(n-1) + fibo(n-2) #n이 0, 1이 될 때까지 작동해서 값을 구해옴.

n = 5
fibonbr = fibo(n)
print(fibonbr)
'''

secs = int(input())
d = secs//86400
secs%=86400
h = secs // 3600
secs%=3600
m = secs // 60
s = secs % 60

time = []
a = ''

# 아래 공간에 프로그램을 완성하세요.
if d > 0:
    a = ("{}:day".format(d))
    time.append(a)
if h > 0:
    a = ("{}:hour".format(h))
    time.append(a)
if m > 0:
    a = ("{}:min".format(m))
if s < 60:
    a = ("{}:second".format(s))
    time.append(a)


print(time)
