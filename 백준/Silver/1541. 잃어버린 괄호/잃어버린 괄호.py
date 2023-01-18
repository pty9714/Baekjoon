a= input()
for i in range(len(a)):
    if a[i] == '-':
        l = a[:i]
        j=list(map(int,l.split('+')))
        m = a[i+1:]
        m=m.replace('-','+')
        k=list(map(int,m.split('+')))
        print(sum(j)-sum(k))
        break
else:
    j=list(map(int,a.split('+')))
    print(sum(j))
