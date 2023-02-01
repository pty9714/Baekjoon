
num = int(input())
l = list(map(int,input().split()))
a = int(input())
for _ in range(a):
    x,y = map(int,input().split())
    if x == 1:
        for i in range(y-1,num,y):
            l[i] = int (not bool(l[i]))

    else:
        l[y-1] = int (not bool(l[y-1]))
        for k in range(num//2):
            if y-1 +k > num-1 or y-1-k<0 :
                break
            if l[y-1+k] == l[y-1-k]:
                l[y-1+k] = int (not bool(l[y-1+k]))
                l[y-1-k] = int (not bool(l[y-1-k]))
                k+=1
            else:
                break

for i in range(len(l)):
    print(l[i],end = ' ')
    if (i+1)%20 == 0:
        print()