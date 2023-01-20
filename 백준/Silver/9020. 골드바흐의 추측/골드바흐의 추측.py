a = int(input())
for _ in range(a):
    b = int(input())
    if b==4:
        print('2 2')
        continue
    else:
        lst = [True]*(b+1)
        lst[1] = False
        for i in range(2,int(b**(1/2))+1):
            if lst[i]==True:
                for j in range(2*i,b+1,i):
                    lst[j] = False

        l = []
        for i in range(2,b+1):
            if lst[i]==True:
                l.append(i)

        for i in range(b//2,b):
            if i in l and b-i in l:
                print (b-i,i)
                break