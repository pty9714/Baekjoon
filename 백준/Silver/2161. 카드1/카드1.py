l = [x for x in range(1,int(input())+1)]
while len(l) !=1:
    print(l[0],end=' ')
    l.pop(0)
    x = l[0]
    l.pop(0)
    l.append(x)
print(l[0])