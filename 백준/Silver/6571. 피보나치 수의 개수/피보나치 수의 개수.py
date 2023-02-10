l = [1,2]
while True:
    k = l[-2]+l[-1]
    l.append(k)

    if k>=10**100:
        break

while True:
    a,b=map(int,input().split())
    if a==0 and b==0:
        break

    cnt = 0
    for i in l:
        if a<=i<=b:
            cnt+=1

    print(cnt)