#1929
a,b = map(int,input().split())
lst = [True]*(b+1)
lst[1] = False
for i in range(2,int(b**(1/2))+1):
    if lst[i]==True:
        for j in range(2*i,b+1,i):
            lst[j] = False

for i in range(a,b+1):
    if lst[i]==True:
        print(i)

