
a = int(input())
for i in range(a):
    x,y = map(int,input().split())
    print(f'#{i+1} {x//y} {x%y}')