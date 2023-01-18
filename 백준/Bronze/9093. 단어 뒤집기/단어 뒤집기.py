num = int(input())
for i in range(num):
    l = list(input().split())
    for j in l:
        print(j[::-1],end=' ')
    print('')