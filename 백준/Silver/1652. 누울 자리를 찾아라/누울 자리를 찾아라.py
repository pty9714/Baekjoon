import sys
input = sys.stdin.readline
import copy
l = []
N = int(input())
for _ in range(N):
    l.append(list(input().rstrip()))

l2 = copy.deepcopy(l)
cnt1=0
cnt2=0
for i in range(N):
    for j in range(N-1):
        if l[i][j] == '.' and l[i][j+1] == '.':
            cnt1 +=1
            k = 1
            try:
                while l[i][j+k] == '.':
                    l[i][j+k] = 'X'
                    k+=1
            except:
                continue

for i in range(N-1):
    for j in range(N):
        if l2[i][j] == '.':
            if l2[i+1][j] == '.':
                cnt2 +=1  
                k = 1
                try:
                    while l2[i+k][j] == '.':
                        l2[i+k][j] = 'X'
                        k+=1
                except:
                    continue

print(cnt1,cnt2)