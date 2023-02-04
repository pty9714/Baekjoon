a,b = map(int,input().split())
l = []
for _ in range(a):
    l.append(int(input()))
result = []
start = 0
end = max(l)
while start<=end and end!=0:
    total = 0
    mid = (start+end)//2
    if mid == 0:
        mid +=1
    for i in l:
        if i>=mid:
            total += i//mid
    
    if total<b:
        end=mid-1
    else:
        result.append(mid)
        start = mid+1

print(max(result))