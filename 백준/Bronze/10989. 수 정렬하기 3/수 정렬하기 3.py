import sys
input = sys.stdin.readline
a = int(input())

l1 = [0]*10000
for i in range(a):
    k = int(input())
    l1[k-1] += 1

for i in range(len(l1)):
    if l1[i] !=0:
        for j in range((l1[i])):
            print(i+1)