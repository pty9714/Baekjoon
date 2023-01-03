list1 = []
for i in range(10):
    a = int(input())
    list1.append(a)
    list1[i] = list1[i]%42

s = set(list1)

print(len(s))
