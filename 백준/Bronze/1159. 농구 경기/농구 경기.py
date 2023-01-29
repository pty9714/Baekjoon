tc = int(input())
d = {}
for i in range(tc):
    a = input()
    d[a[0]] = d.get(a[0],0)+1

l = list(d.items())
l = sorted(l,key = lambda x: x[0])
check = 0
for i in l:
    if i[1]>=5:
        print(i[0],end='')
        check = 1

if check == 0:
    print('PREDAJA')