n,m = map(int,input().split())
l = list(map(int,input().split()))
l = list(set(l))
l.sort()

def bt(lst,cnt):
    if cnt == m:
        print(*lst)
        return
    idx = l.index(lst[-1])
    for i in range(idx,len(l)):
        lst.append(l[i])
        bt(lst,cnt+1)
        lst.pop()

for i in l:
    bt([i],1)
    