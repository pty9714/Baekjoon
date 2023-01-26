l = [25,10,5,1]
for _ in range(int(input())):
    m = int(input())*1
    for i in l:
        if m >= i:
            print(m//i,end=' ')
            m%=i 
        else:
            print('0',end=' ')