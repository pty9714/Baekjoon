a= int(input())
arr = []
for i in range(6):
    arr.append(list(map(int,input().split())))

x=0
y=0
x_idx = 0
y_idx = 0
for i in range(6):
    if arr[i][0] == 1 or arr[i][0] ==2:
        if x < arr[i][1]:
            x = arr[i][1]
            x_idx = i
    elif arr[i][0] == 3 or arr[i][0] ==4:
        if y < arr[i][1]:
            y = arr[i][1]
            y_idx = i

y_short = abs(arr[(x_idx-1)%6][1]-arr[(x_idx+1)%6][1])
x_short = abs(arr[(y_idx-1)%6][1]-arr[(y_idx+1)%6][1])
print((x*y-x_short*y_short)*a)