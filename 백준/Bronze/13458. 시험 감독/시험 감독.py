import math
num = int(input())
l = list(map(int,input().split()))
m,n = map(int,input().split())
sum = 0
for i in range(len(l)):
    if l[i]-m>0:
        sum +=math.ceil((l[i]-m)/n)+1
    else:
        sum +=1
print(sum)