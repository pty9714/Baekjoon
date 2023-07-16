num = int(input())

d1 = [(1, 0), (-1, 0), (0, 1), (0, -1)]
d2 = [(1, 1), (1, -1), (-1, -1), (-1, 1)]

for tc in range(1, num + 1):
    n, m = map(int, input().split())

    l = []
    maxf = 0
    for i in range(n):
        l.append(list(map(int, input().split())))

    for x in range(n):
        for y in range(n):
            p = l[y][x]
            d = l[y][x]
            for i in range(1, m):
                for mx, my in d1:
                    if 0 <= x + mx * i < n and 0 <= y + my * i < n:
                        p += l[y + my * i][x + mx * i]

            for i in range(1, m):
                for mx, my in d2:
                    if 0 <= x + mx * i < n and 0 <= y + my * i < n:
                        d += l[y + my * i][x + mx * i]

            maxf = max(maxf, p, d)

    print(f'#{tc} {maxf}')