a= int(input())
for i in range(a):
    b = int(input())
    l = ['close'] * (b+1)
    for j in range(1,b+1):
        k=j
        while k<=b:
            if l[k] == 'close':
                l[k] = 'open'
                k+=j
            elif l[k] == 'open':
                    l[k] ='close'
                    k+=j
    print(l.count('open'))