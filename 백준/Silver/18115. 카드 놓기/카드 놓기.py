from collections import deque
a = int(input())
l = list(map(int,input().split()))
numl = [i for i in range(1,a+1)]
ans = []
deq = deque([])
ans2 = deque([])
a = len(l)
for i in range(a):
    if l[i] == 1:
        if deq:
            deq.appendleft(numl.pop())
            ans +=deq
            deq = deque([])
        else:
            ans.append(numl.pop())
    elif l[i] == 2:
        a = numl.pop()
        deq.append(a)
    else:
        ans2.appendleft(numl.pop())

print(*(ans),end=' ')
if deq:
    print(*(deq),end=' ')
print(*(ans2),end=' ')