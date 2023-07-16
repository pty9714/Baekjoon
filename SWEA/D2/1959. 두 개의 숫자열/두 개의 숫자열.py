num = int(input())
for i in range(num):
    n,m = map(int,input().split())
    l1 = list(map(int, input().split()))
    l2 = list(map(int, input().split()))
    
    if len(l1)>=len(l2):
        min_len = len(l2)
        max_len = len(l1)
    else:
        min_len = len(l1)
        max_len = len(l2)
   
    check = 0
    for j in range(min_len):
        check += l1[j]*l2[j]
    

    if len(l1) == len(l2):
        max = check

    elif min_len == len(l1):
        max = check
        for j in range(max_len-min_len+1):
            check = 0
            for k in range(min_len):
                check += l1[k]*l2[k+j]

            if max<check:
                max = check    
    else:
        max = check
        for j in range(max_len-min_len+1):
            check = 0
            for k in range(min_len):
                check += l1[k+j]*l2[k]

            if max<check:
                max = check    


    print(f"#{i+1} {max}")
        
    