l2 = []
for i in range(5):
    l = list(map(int,input().split()))
    l2.append(sum(l))
print(l2.index(max(l2))+1,max(l2))