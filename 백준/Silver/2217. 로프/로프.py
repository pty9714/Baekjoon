a = int(input())
l = []
for i in range(a):
    l.append(int(input()))
l = sorted(l)
j = []
for i in range(a):
    j.append(l[0]*a)
    l.pop(0)
    a-=1

print(max(j))