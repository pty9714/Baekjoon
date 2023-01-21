while True:
    try:
        k = 1
        a= int(input())
        while k%a != 0:
            k = k*10+1
        print(len(str(k)))
    except EOFError:
        break