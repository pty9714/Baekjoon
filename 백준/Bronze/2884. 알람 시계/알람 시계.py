num1,num2 = map(int, input().split())
if num2<45:
    if num1==0:
        num1 = 23
        num2 +=15
    else:
        num1 -=1
        num2 +=15
else:
    num2 -=45
print(num1,num2)