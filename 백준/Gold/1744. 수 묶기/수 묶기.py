import sys
input = sys.stdin.readline

num = int(input())
total = 0
minusl = []
plusl = []
zero_check = False
for i in range(num):
    a = int(input())
    if a>0:
        plusl.append(a)
    elif a<0:
        minusl.append(a)
    else:
        zero_check=True

plusl.sort(reverse=True)
minusl.sort()
if len(plusl)%2==0:
    for i in range(len(plusl)//2):
        a= plusl[2*i]
        b= plusl[2*i+1]
        if a == 1 or b == 1:
            total +=a+b
        else:
            total +=a*b
else:
    for i in range(len(plusl)//2):
        a= plusl[2*i]
        b= plusl[2*i+1]
        if a == 1 or b == 1:
            total +=a+b
        else:
            total +=a*b
    total += plusl[-1]

if len(minusl)%2==0:
    for i in range(len(minusl)//2):
        a= minusl[2*i]
        b= minusl[2*i+1]
        total +=a*b
else:
    for i in range(len(minusl)//2):
        a= minusl[2*i]
        b= minusl[2*i+1]
        total +=a*b
    if zero_check == False:
        total += minusl[-1]


print(total)