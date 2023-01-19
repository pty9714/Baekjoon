a = int(input())
d = {}
for i in range(a):
    name, atd = input().split()
    if atd == 'enter':
        d[name] = 1
    elif atd == 'leave':
        d[name] = 0
l = []
for key, value in d.items():
    if value == 1:
        l.append(key)
l.sort(reverse=True)
print(*l,sep='\n')