
a = int(input())
for i in range(a):
    x = list(map(int,input().split()))
    print(f'#{i+1} {max(x)}')