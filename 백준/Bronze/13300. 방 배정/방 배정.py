import math

num, cnt = map(int,input().split())
list0 = [0]*6
list1 = [0]*6

for i in range(num):
    a,b = map(int,input().split())
    if a == 0:
        list0[b-1] += 1
    else:
        list1[b-1] += 1


room = 0

for i in range(6):
    room += math.ceil(list0[i]/cnt)
    room += math.ceil(list1[i]/cnt)

print(room)