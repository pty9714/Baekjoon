import sys
input = sys.stdin.readline
a = int(input())
total = 0
for i in range(a):
    total +=int(input())


print(total+1-a)