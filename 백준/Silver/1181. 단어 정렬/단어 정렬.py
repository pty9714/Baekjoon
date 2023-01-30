a = int(input())
L = []
for i in range(a):
    x= input()
    L.append(x)
L = list(set(L))
L.sort(key = lambda x: (len(x),x))

for i in L:
  print(i)
