a = int(input())

for i in range(a):
    p = 0
    x,y = map(int,input().split())
    if x==0:
        pass
    elif x==1:
        p+=5000000
    elif x<=3:
        p+=3000000
    elif x<=6:
        p+=2000000
    elif x<=10:
        p+=500000
    elif x<=15:
        p+=300000
    elif x<=21:
        p+=100000
    if y==0:
        pass
    elif y==1:
        p+=5120000
    elif y<=3:
        p+=2560000
    elif y<=7:
        p+=1280000
    elif y<=15:
        p+=640000
    elif y<=31:
        p+=320000
    print(p)