num1 = int(input())
num2 = int(input())
a = []
for j in range(num1,num2+1):
    if j == 1: # 1예외처리
        continue
    for i in range(2,j+1):
        if j == i: #리스트에 소수 입력
            a.append(j)
        if j%i == 0: # 합성수일 경우 break
            break
if len(a) == 0:
    print('-1') #소수가없는경우 -1 출력
else:
    print(sum(a))
    print(a[0])