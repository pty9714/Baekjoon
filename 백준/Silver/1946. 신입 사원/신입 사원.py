import sys
input = sys.stdin.readline
test_case = int(input())

for _ in range(test_case):
    num = int(input())
    l = []
    for _ in range(num):
        a,b = map(int,input().split())
        l.append([a,b])
    l = sorted(l,key = lambda x:x[0])
    k = l[0][1]
    cnt = 1
    for j in range(1,num):
        if l[j][1]<k:
            cnt +=1
            k = l[j][1]

    print(cnt)