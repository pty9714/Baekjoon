import sys
input = sys.stdin.readline
a, b = map(int,input().split())
l = {}
for i in range(1,a+1):
    s = input().rstrip()
    l[s] = i
    l[i] = s
    
for j in range(b):
    k = input().rstrip()
    if k.isdigit() == True :

        print(l[int(k)])
    else:
        print(l[k])