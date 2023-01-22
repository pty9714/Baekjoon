l1 = list(map(int,input().split()))
l2 = list(map(int,input().split()))

if sum(l1)>sum(l2):
    print(sum(l1))
else:
    print(sum(l2))