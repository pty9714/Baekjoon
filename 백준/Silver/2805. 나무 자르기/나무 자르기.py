a,b = map(int,input().split())
l = list(map(int,input().split()))
result = []
start = 0
end = max(l)
while start<=end:
    total = 0
    mid = (start+end)//2
    for i in l:
        if i>mid:
            total += i-mid
    
    if total<b:
        end=mid-1
    else:
        result=mid
        start = mid+1

print(result)