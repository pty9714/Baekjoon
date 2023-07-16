num = int(input())
for tc in range(1,num+1):
    n = int(input())
    l = []
    l90 = [[0]*n for _ in range(n)]
    l180 = [[0]*n for _ in range(n)]
    l270 = [[0]*n for _ in range(n)]

    for i in range(n):
        l.append(list(map(int,input().split())))

    
    for i in range(n):
        for j in range(n):
            l90[j][n-1-i] = l[i][j]
            l180[i][j] = l[n-1-i][n-1-j]
            l270[n-1-j][i] = l[i][j]

    print(f'#{tc}')
    for i in range(n):
        print(''.join(map(str, l90[i])),end=' ')
        print(''.join(map(str, l180[i])),end=' ')
        print(''.join(map(str, l270[i])))