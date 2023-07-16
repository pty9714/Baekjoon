num = int(input())
for i in range(num):
    check = 0
    l = []
    for j in range(9):
        l.append(list(map(int,input().split())))
    
    for j in range(9):
        s = 0
        for k in range(9):
            s += l[k][j]

        if s != 45 or sum(l[j]) != 45:
            check+=1
            break

    for j in range(3):
        for k in range(3):
            s = 0 
            for x in range(3):
                for y in range(3):
                    s += l[x+3*j][y+3*k]
            
            if s != 45:
                check +=1
                break




    if check==0:        
        print(f"#{i+1} 1")
    else:
        print(f"#{i+1} 0")