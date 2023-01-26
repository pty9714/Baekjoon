#2161
l = [x for x in range(1,int(input())+1)]
while len(l) !=1:
    print(l.pop(0),end=' ')
    l.append(l.pop(0))
print(l[0])