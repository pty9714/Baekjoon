a = input()
l = []
for i in range(0,len(a)):
    l.append(a[i:len(a)])
for i in sorted(l):
    print(i)
