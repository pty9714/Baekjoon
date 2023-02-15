from collections import deque
st,ed = map(int,input().split())
check = [False]*(100001)
def bfs(st,ed):
    deq = deque([(st,0)])
    
    while deq:
        k,cnt = deq.popleft()
        if k == ed:
            print(cnt)
            break
        if 0<=k+1<100001 and check[k+1] == False:
            check[k+1] = True
            deq.append((k+1,cnt+1))
        if 0<=k-1<100001 and check[k-1] == False:
            check[k-1] = True
            deq.append((k-1,cnt+1))
        if 0<=2*k<100001 and check[2*k] == False:
            check[2*k] = True
            deq.append((2*k,cnt+1))

    

bfs(st,ed)
