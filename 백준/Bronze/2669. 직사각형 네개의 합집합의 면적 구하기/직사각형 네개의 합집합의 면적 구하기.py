#2669
check = [[False]*100 for _ in range(100)]
for _ in range(4):
    a,b,c,d = map(int,input().split())
    for i in range(a,c):
        for j in range(b,d):
            check[i][j] = True
           
total = 0
for i in range(100):
    total += check[i].count(True)
print(total)
