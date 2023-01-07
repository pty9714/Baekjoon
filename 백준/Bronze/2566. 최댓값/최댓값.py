a = []
for i in range(9) :
    a.append(list(map(int,input().split())))

max = a[0][0]
x_pos = 0
y_pos = 0
for i in range(9):
    for j in range(9):
        if max<a[i][j]:
            max = a[i][j]
            x_pos = i
            y_pos = j

print(max)
print(x_pos+1, y_pos+1)