for i in range(int(input())):
    l = list(map(int,input().split()))
    k = []
    for i in l:
        if i%2 ==0:
            k.append(i)
    
    print(sum(k),min(k))