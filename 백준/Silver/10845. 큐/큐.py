from collections import deque
import sys
input = sys.stdin.readline
tc = int(input())
q = deque()
for _ in range(tc):
    a = input().rstrip()
    if a == 'front':
        try: 
            print(q[0]) 
        except: 
            print('-1') 
            continue
    elif a == 'back':
        try: 
            print(q[-1]) 
        except: 
            print('-1')
            continue
    elif a == 'size':
        print(len(q))
    elif a == 'empty':
        if q: 
            print(0)
        else: 
            print(1)
    elif a == 'pop':
        try: 
            print(q.popleft())
        except: 
            print('-1')
            continue
    else:
        x,y = a.split()
        q.append(y)