a, b = map(int,input().split())
i1 = []
j1 = []

for i in range(a):
    k1 = list(map(int,input().split()))
    i1.append(k1)

for j in range(a):
    k1 = list(map(int,input().split()))
    j1.append(k1)
 
for i in range(a):
    for j in range(b):
        i1[i][j] +=j1[i][j]

for i in range(a):
    for c in i1[i]:
        print(c, end = ' ')

    print()   