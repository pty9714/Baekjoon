a = int(input())
while a !=0:
    lst = [True]*(2*a+1)
    lst[1] = False
    for i in range(2,int((2*a)**(1/2))+1):
        if lst[i]==True:
            for j in range(2*i,2*a+1,i):
                lst[j] = False
    cnt = 0
    for i in range(a+1,2*a+1):
        if lst[i]==True:
            cnt+=1
    print(cnt)
    a = int(input())

