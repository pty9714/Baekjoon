def gcd(x,y):
    while y>0:
        x,y=y,x%y
    return x

def gcdlist(lst):
    k=lst[0]
    for i in lst:
        k = gcd(k,i)
        if k == 1:
            break
    return k

l1 = []
l2 = []
for _ in range(int(input())):
    l1.append(int(input()))

for i in range(len(l1)-1):
    l2.append(l1[i+1]-l1[i])


cnt = 0
g = gcdlist(l2)
for i in l2:
    cnt += i//g-1

print(cnt)