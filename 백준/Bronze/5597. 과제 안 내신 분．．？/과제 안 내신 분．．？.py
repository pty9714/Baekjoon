list = []
for i in range(28):
    a = int(input())
    list.append(a)

list.sort()
if list[0] == 2:
    print ('1')

if list[0] == 3:
    print ('1')
    print ('2')

for i in range(27):
    if list[i+1]-list[i] == 2:
        print(list[i+1]-1)
    elif list[i+1]-list[i] == 3:
        print(list[i+1]-2)
        print(list[i+1]-1)

if list[-1] == 29:
    print('30')

if list[-1] == 28:
    print('29')
    print('30')