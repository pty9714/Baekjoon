import sys
input = sys.stdin.readline
a = int(input())
for i in range(a):
    b = input().rstrip()
    cnt = 0
    for i in b:
        if i == '(':
            cnt +=1
        elif i == ')':
            cnt -=1
        if cnt<0:
            print('NO')
            break
    else:
        if cnt == 0 :
            print('YES')
        else : 
            print('NO')