while True:
    a = int(input())
    if a == -1:
        break
    else:
        l = set([])
        for i in range(1,int(a**(1/2))+1):
            if a%i == 0:
                l.add(i)
                l.add(a//i)
        l.remove(a)
        k = sorted(l)
        if a == sum(l):
            print(str(a)+' = ',end='')
            print(*k,sep=' + ')
        else:
            print(f'{a} is NOT perfect.')