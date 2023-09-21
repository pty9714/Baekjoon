a,b = map(int,input().split())
cnt =0 
flag = False
while a!=b:
    if a>b:
        print(-1)
        flag = True
        break

    if b%2==0:
        b //= 2
    elif (b-1)%10 ==0 :
        b = (b-1)//10
    else:
        print(-1)
        flag = True
        break

    cnt +=1

if flag == False:
    print(cnt+1)