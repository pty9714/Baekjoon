def gcd(x,y):
    while(y):
        x,y = y,x%y
    return x


a = int(input())
l = list(map(int,input().split()))
for i in range(1,a):
    x = gcd(l[0],l[i])
    print(f'{int(l[0]/x)}/{int(l[i]/x)}')