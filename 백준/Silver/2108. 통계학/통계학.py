
import sys
def input() : return sys.stdin.readline().rstrip()

a = int(input())
L = []
for i in range(a):
    L.append(int(input()))    

L.sort()

print(round(sum(L)/a))
print(L[int((a-1)/2)])

k = []
dic = {}
for i in L:
    if i not in dic:
        dic[i] = 1
    elif i in dic:
        dic[i] +=1

for key, value in dic.items():
    if value == max(dic.values()):
        k.append(key)

if len(k) == 1:
    print (k[0])

elif len(k) >1:
    k.sort()
    print(k[1])

print(L[-1]-L[0])