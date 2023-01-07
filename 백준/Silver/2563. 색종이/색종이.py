a = int(input())
b = []
c = []
for i in range(a) :
    b.append(list(map(int,input().split())))

for i in range(a):
    for j in range(b[i][0],b[i][0]+10):
        for k in range(b[i][1],b[i][1]+10):
            if [j,k] in c:
             continue
            c.append([j,k])
    
print(len(c))  