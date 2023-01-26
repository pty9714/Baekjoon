from collections import deque

import sys
# sys.stdin = open('input.txt','r')
input = sys.stdin.readline
a= int(input())
l = deque()
for i in range(a):
    string = input().rstrip()
    if string == 'front':
        try: 
            print(l[0])
        except:
            print(-1)
            continue
    elif string == 'back':
        try: 
            print(l[-1])
        except:
            print(-1)
            continue
    elif string == 'size':
        print(len(l))
    elif string == 'empty':
        if len(l)==0:
            print(1)
        else:
            print(0)
    elif string == 'pop':
        try:
            print(l[0])
            l.popleft()
        except:
            print(-1)
            continue
    else:
        x,y = string.split()
        l.append(y)