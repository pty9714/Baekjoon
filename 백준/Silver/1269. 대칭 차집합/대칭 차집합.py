a,b = map(int,input().split())
l1 = list(map(int,input().split()))
l2 = list(map(int,input().split()))
k = {}
for i in l1:
    if i not in k:
        k[i] = 1
    else:
        k[i] +=1
for i in l2:
    if i not in k:
        k[i] = 1
    else:
        k[i] +=1
count = 0
for j in k:
    if k[j]==1:
        count +=1
print (count)