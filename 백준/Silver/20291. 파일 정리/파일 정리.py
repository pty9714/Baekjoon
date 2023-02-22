import sys
input = sys.stdin.readline

dic = {}
l = []
for _ in range(int(input())):
    a,b = input().rstrip().split('.')
    dic[b] = dic.get(b,0)+1


for a,b in dic.items():
    l.append((a,b))

l.sort()

for a,b in l:
    print(a,b)