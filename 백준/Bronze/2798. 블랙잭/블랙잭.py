import sys
input = sys.stdin.readline
a,b = map(int,input().split())
l = list(map(int,input().split()))
sum_list= []
for i in range(0,a):
    for j in range(0,a):
        for k in range(0,a):
            if i!=j and j!=k and k!=i:
                sum = l[i]+l[j]+l[k]
                sum_list.append(sum)

m = 0
for i in range(len(sum_list)):
    if sum_list[i]<=b and m<sum_list[i]:
        m = sum_list[i]

print(m)