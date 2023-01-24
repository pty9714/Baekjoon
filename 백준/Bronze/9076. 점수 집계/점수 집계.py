a = int(input())
for i in range(a):
    l = list(map(int,input().split()))
    l = sorted(l)
    if l[-2]-l[1] >=4:
        print('KIN')
    else:
        print(sum(l[1:-1]))