a,b = map(int,input().split())
chi =  2*int(input())

if a+b>=chi:
    print(a+b-chi)
else:
    print(a+b)