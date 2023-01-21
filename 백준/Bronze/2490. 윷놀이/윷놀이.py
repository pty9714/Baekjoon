
for i in range(3):
    l = list(map(int,input().split()))
    if sum(l) == 4:
        print('E')
    else:
        print(chr((ord('A')-sum(l))+3))