A = input()
listA = [A[i] for i in range(3)] # 리스트를 반복문으로 생성
listA = [int(i) for i in listA] # str 타입의 문자열을 int 타입으로 변환

B = input()
listB = [B[i] for i in range(3)]
listB = [int(i) for i in listB]

for i in range(3):
    calc = (listA[0] * 100 * listB[2 - i]) + (listA[1] * 10 * listB[2 - i]) + (listA[2] * listB[2 - i])
    print(calc)

print(int(A) * int(B))
