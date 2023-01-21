a = int(input())
for i in range(a):
    b = int(input())
    b = str(format(b,'b'))
    for i in range(len(b)-1,-1,-1):
        if b[i] == '1':
            print (len(b)-i-1)
