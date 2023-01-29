import sys
input = sys.stdin.readline
tc = int(input())
cnt = 0
for _ in range(tc):
    s = input().rstrip()
    l = []
    for i in s:
        try:
            if i == l[-1]:
                l.pop()
            else:
                l.append(i)
        except:
            l.append(i)
    if not l:
        cnt +=1
print(cnt)
        