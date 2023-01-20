a = input()
k=0
while a != '1':
    for i in a:
        k +=int(i)**2
    a = str(k)
    k = 0

    if a == '4':
        print('UNHAPPY')
        break

if a!='4':
    print('HAPPY')