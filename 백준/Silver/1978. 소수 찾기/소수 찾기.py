num = int(input())
count = 0
a = list(map(int,input().split()))
for j in range(num):
    if a[j] == 1:
        count+=1
        continue
    for i in range(2,a[j]):
        if a[j]%i == 0: 
            count+=1
            break
print(num - count)