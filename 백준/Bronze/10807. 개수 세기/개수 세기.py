a = int(input())
L = list(map(int, input().split()))
count = 0
b = int(input())
for i in range(a):
    if b == L[i]:
        count +=1

print (count)
