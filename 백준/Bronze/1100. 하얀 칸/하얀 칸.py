l = []
for i in range(8):
    a = list(input())
    l.append(a)
cnt = 0
for i in range(8):
    for j in range(8):
        if (i+j)%2==0 and l[i][j] == 'F':
            cnt +=1
print(cnt)