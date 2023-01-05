num1 = int(input())
d = 2
while num1!=1:
    if num1%d == 0:
        print (d)
        num1 //=d
    
    else:
        d+=1