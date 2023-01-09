num= int(input())
k = []
for i in range(num):
    a,b = map(str,input().split())
    a= int(a)
    k.append([a,b,i])

k.sort(key = lambda k:(k[0],k[2]))

for i in range(num):
    print(k[i][0],k[i][1])