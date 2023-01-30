#1225
a,b = input().split()
a_l = list(map(int,a))
a = sum(a_l)
total = 0
for j in b:
    total +=a*int(j)
print(total)