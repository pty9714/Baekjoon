a = int(input())
L = set([])
for i in range(a):
    x= input()
    L.add(x)
L = list(L)
L.sort(key = lambda x: (len(x),x))

for i in L:
  print(i)
