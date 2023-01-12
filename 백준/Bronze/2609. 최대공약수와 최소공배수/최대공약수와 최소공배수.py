a,b = map(int,input().split())
n=2
m=1
while a>=n or b>=n:
    if a%n == 0 and b%n == 0:
        a/=n
        b/=n
        m*=n
    else:
        n+=1

print(m)
print(int(m*a*b))