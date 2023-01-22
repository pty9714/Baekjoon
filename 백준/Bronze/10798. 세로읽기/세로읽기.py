l = []
length = []
for i in range(5):
    a = input()
    l.append(a)
    length.append(len(a))

for j in range(max(length)):
    for k in range(5):
        try:
            print(l[k][j],end='')
        except:
            continue