num1,num2 = map(int, input().split())
min = int(input())

hour = min//60
min = min%60
if num2+min<60:
    print ((num1+hour)%24,(num2+min))
else:
    print ((num1+hour+1)%24,(num2+min)%60)