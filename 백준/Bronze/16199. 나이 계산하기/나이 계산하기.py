d1 = list(map(int,input().split()))
d2 = list(map(int,input().split()))

if d2[1]>d1[1]:
    print(d2[0]-d1[0])
elif d2[1] == d1[1] :
    if d2[2] >= d1[2]:
        print(d2[0]-d1[0])
    else:
        print(d2[0]-d1[0]-1)
else:
    print(d2[0]-d1[0]-1)  


print(d2[0]-d1[0]+1) 
print(d2[0]-d1[0]) 
