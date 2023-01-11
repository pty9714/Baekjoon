
a= int(input())
arr = []
for i in range(a):
    arr.append(list(map(int,input().split())))
for i in range(a):
    count = 1
    for j in range(a):
        if arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1]:
            count +=1
    print (count)