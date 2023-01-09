
import sys
input = sys.stdin.readline
num= int(input())
k = list(map(int,input().split()))

dic = {}
l = sorted(list(set(k)))

for i in range(len(l)):
    dic[l[i]] = i
for i in k:
    print (dic[i],end=' ')