a,b = map(int,input().split())
l = []
for i in range(a):
    li= list(input())
    l.append(li)

cnt = a*b
for i in l:
    for j in range(1,b):
        if i[j]=='-' and i[j]==i[j-1]:
            cnt-=1
    
for i in range(1,a):
    for j in range(0,b):
        if l[i][j] == '|' and l[i][j]==l[i-1][j]:
            cnt-=1
print(cnt)