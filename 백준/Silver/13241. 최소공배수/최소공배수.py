def gcd(x,y):
    while y>0:
        x,y=y,x%y
    return x


n1, n2 = map(int,input().split())
print(n1*n2//gcd(n1,n2))