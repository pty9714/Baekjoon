a = int(input())
L = []
for i in range(a):
    x= input()
    if x not in L:
        L.append(x)

L.sort(key = lambda x: (len(x),x))

for i in L:
  print(i)