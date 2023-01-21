a = int(input())
for j in range(1,a+1):
    print((a-j)*' ',end='')
    for i in range(2*j):
        if i%2==0:
            print('*',end='')
        else:
            print(' ',end='')
    print('')