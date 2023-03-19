lst = []
a =  int(input())
for i in range(a):
    lst.append(int(input()))


result = [0]*a
result[0] = lst[0]
if a>=2: 
    result[1] = lst[0]+lst[1]
if a>=3:     
    result[2] = max(lst[0]+lst[2],lst[1]+lst[2],lst[0]+lst[1])
if a>=4:
    for j in range(3,a):
        result[j] = max(lst[j]+result[j-2],lst[j]+lst[j-1]+result[j-3])
        result[j] = max(result[j-1],result[j])

print(max(result))