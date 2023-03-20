a,b=map(int, input().split())

if a<=b:
    print((a+b)*(b-a+1)//2)

else:
    print((a+b)*(a-b+1)//2)