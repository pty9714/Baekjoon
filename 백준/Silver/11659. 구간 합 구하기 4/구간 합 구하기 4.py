import sys
input = sys.stdin.readline
N,M = map(int,input().split())
l = list(map(int,input().split()))

# for i in range(M):
#     x, y= map(int,input().split())
#     sum = 0
#     for i in range(x-1,y):
#         sum += l[i]
#     print(sum)   
sum = 0
sum_list = [0]
for i in l:
    sum +=i
    sum_list.append(sum)
for i in range(M):
    x,y= map(int,input().split())
    print(sum_list[y]-sum_list[x-1])