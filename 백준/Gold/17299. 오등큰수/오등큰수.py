import sys
input = sys.stdin.readline
a = int(input())
l = list(map(int,input().split()))
d = {}
for i in l:
    d[i] = d.get(i,0)+1
answer = [-1] * a
stack = []

stack.append(0)
for i in range(1,a):
    while stack and d[l[stack[-1]]] < d[l[i]]:
        answer[stack.pop()] = l[i]
    stack.append(i)
print(*answer)