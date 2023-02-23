a = input()
def p(a):
    if a == '1':
        return('2')
    else:
        while True:
            b = ''
            for i in a:
                b = i+b
            if a == b:
                for j in range(2,int(int(a)**(1/2))+1):
                    if int(a)%j==0:
                        a = str(int(a)+1)
                        break
                else:
                    return(a)
            else:
                a = str(int(a)+1)

print(p(a))