num =  int(input())
a=0
b=0
c=0
if num>=300:
    a=num//300 
    num%=300

if num>=60:
    b= num//60
    num%=60

if num>=10:
    c= num//10
    num%=10

if num>0:
    print(-1)
else:
    print(a,b,c)