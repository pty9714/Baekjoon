a = int(input())
if a%5 == 0:
    print (int(a/5))
elif (a-3)%5== 0 and a-3>0 :
    print (int((a-3)/5+1))
elif (a-6)%5== 0 and a-6>0:
    print (int((a-6)/5+2))
elif (a-9)%5== 0 and a-9>0 :
    print (int((a-9)/5+3))
elif (a-12)%5== 0 and a-12>0:
    print (int((a-12)/5+4))
elif a%3 == 0:
    print (int(a/3))
else:
    print ('-1')
