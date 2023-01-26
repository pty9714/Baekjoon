from collections import deque
a,b = map(int,input().split())
l = deque(x for x in range(1,a+1))
l_new=[]
while len(l) !=1:
    for i in range(b-1):
        l.append(l.popleft())

    l_new.append(l.popleft())    
l_new.append(l[0])

result = ', '.join(map(str,l_new))
print(f'<{result}>')