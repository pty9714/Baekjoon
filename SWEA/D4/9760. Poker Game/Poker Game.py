n = int(input())
for i in range(1,n+1):
    l = list(input().split())
    l1 = []
    l2 = []
    check = [0]*14
    for j in l:
        l1.append(j[0])
        l2.append(j[1])
    
    
    for j in range(5):
        if l2[j] == 'A':
            l2[j] = 1
        elif l2[j] == 'T':
            l2[j] = 10
        elif l2[j] == 'J':
            l2[j] = 11           
        elif l2[j] == 'Q':
            l2[j] = 12    
        elif l2[j] == 'K':
            l2[j] = 13
        else:
            l2[j] = int(l2[j])

    l2.sort()
    for j in l2:
        check[j] +=1
    # print(l1)
    # print(l2)
    # print(check)
    #1
    if len(set(l1)) == 1:
        if l2 == [1,10,11,12,13]:
            print(f"#{i} Straight Flush")
            continue
        for k in range(4):
            if l2[k+1]-l2[k] !=1:
                break
        else:
            print(f"#{i} Straight Flush")
            continue
        

    #2
    if 4 in check:
        print(f"#{i} Four of a Kind")
        continue
    
    #3
    if 3 in check and 2 in check:
        print(f"#{i} Full House")
        continue

    #4
    if len(set(l1))==1:
        print(f"#{i} Flush")
        continue

    #5
    if len(set(l1))!=1:
        for k in range(4):
            if l2[k+1]-l2[k] !=1:
                break
        else:
            print(f"#{i} Straight")
            continue

    if len(set(l2))==3:
        #6
        if 3 in check:
            print(f"#{i} Three of a kind")
            continue
        #7
        elif check.count(2)==2:
            print(f"#{i} Two pair")
            continue
    #8
    if 2 in check:
        print(f"#{i} One pair")
        continue
    #9
    print(f"#{i} High card")
    continue






