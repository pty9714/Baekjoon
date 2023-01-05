num = int(input())

for i in range(num):
    a = int(input())
    b = int(input())
    L=[i for i in range(1,b+1)]
    
    for j in range(0,a):
        for k in range (1,b):
            L[k] += L[k-1]

    print(L[-1])