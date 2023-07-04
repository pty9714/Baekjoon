list = []
for i in range(9):
    list.append(int(input()))

list.sort()

for i in range(9):
    for j in range(i+1,9):
        if sum(list)-list[i]-list[j] == 100:
            for k in range(9):
                if k != i and k != j:
                    print(list[k])
            exit()