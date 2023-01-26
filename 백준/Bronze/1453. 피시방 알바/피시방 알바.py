num = int(input())
l = list(map(int,input().split()))
l2 = []
cnt = 0
for i in l:
    if i in l2:
        cnt +=1
    else:
        l2.append(i)
print(cnt)
