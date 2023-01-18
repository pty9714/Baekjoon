L = list(map(int,input().split()))
for b in range(len(L),0,-1):
    for i in range(b-1):
        if L[i] >= L[i+1]:
            temp = L[i]
            L[i] = L[i+1]
            L[i+1] = temp
            print(*L)