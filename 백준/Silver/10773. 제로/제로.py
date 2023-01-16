import sys
input = sys.stdin.readline
a = int(input())
l = [0]
for i in range(a):
    num = int(input().rstrip())
    if num == 0:
        l.pop()
    else:
        l.append(num)

print(sum(l))