a = int(input())
for _ in range(a):
    x,y= map(int,input().split())
    x = x%10
    if x==0:
        print(10)
    else:
        for i in range(2,6):
            if (x**i)%10 == x%10:
                y= y%(i-1)+i-1
                break
        print((x**y)%10)
