l = []
for i in range(1,51):
    for _ in range(1,i+1):
        l.append(i)
total = 0
a,b= map(int,input().split())
for i in range(a,b+1):
    total +=l[i-1]
print(total)