lower = [chr(x) for x in range(ord('a'),ord('z')+1)]
upper = [chr(x) for x in range(ord('A'),ord('Z')+1)]
number = [str(x) for x in range(0,10)]
while True:
    l= [0,0,0,0]
    try:
        a = input()
        for i in a:
            if i in lower:
                l[0] +=1
            elif i in upper:
                l[1] +=1
            elif i in number:
                l[2] +=1
            elif i == ' ':
                l[3] +=1

        print (*l)

    except:
        break