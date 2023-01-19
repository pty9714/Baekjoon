x,y = map(int,input().split())
a= x-1
b =y-1
if a<=b:
    print(a+(a+1)*b)
else:
    print(b+(b+1)*a)