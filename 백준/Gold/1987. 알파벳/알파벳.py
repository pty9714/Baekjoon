dx = [1,-1,0,0]
dy = [0,0,1,-1]
r,c = map(int,input().split())
l = []
answer = 0
check = set()
for i in range(r):
    l.append(list(input()))

def bt(a,b,cnt):
    global answer
    if cnt>answer:
        answer = cnt
    if answer == 26:
        return
    
    for i in range(4):
        ma = a + dx[i]
        mb = b + dy[i]
        if 0<=ma<r and 0<=mb<c:
            if l[ma][mb] not in check:
                check.add(l[ma][mb])
                bt(ma,mb,cnt+1)
                check.remove(l[ma][mb])
                
check.add(l[0][0])
bt(0,0,1)
print(answer)