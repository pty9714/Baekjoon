a = int(input())
l1 = list(map(int,input().split()))
l2 = list(map(int,input().split()))
total = 0
for i in range(a):
    total +=min(l1) *max(l2)
    l1_idx = l1.index(min(l1))
    l2_idx = l2.index(max(l2))    
    l1.pop(l1_idx)
    l2.pop(l2_idx)

print(total)