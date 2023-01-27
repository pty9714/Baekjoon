import sys
input = sys.stdin.readline            
a,b  = map(int,input().split())
l = list(map(int,input().split()))
l2 = list(map(int,input().split()))
print(len(set(l)^set(l2)))