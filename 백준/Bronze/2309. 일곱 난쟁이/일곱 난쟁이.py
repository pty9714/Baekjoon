from itertools import combinations
l = []
for _ in range(9):
    l.append(int(input()))

k = combinations(l,7)
for i in k:
    if sum(i) == 100:
        print(*sorted(i),sep='\n')
        break