a = int(input())
b= int(input())
c = int(input())
if a+b+c !=180:
    print('Error')
else:
    if a!=b and b!=c and c!=a:
        print('Scalene')
    elif a^b^c==60:
        print('Equilateral')
    else:
        print('Isosceles')