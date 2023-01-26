num = int(input())
l = []
for _ in range(num):
    l.append(list(map(int,input().split())))

l = sorted(l,key = lambda x : (x[1], x[0]))
cnt = 0
end = 0
for i in l:
    if end<=i[0]:
        cnt +=1
        end = i[1]
print(cnt)