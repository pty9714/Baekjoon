test_case = int(input())
for _ in range(test_case):
    k = input()
    num = int(input())
    a = input()
    if a == '[]':
        l = []
    else:
        a = a.strip('[]')
        l  = list(a.split(','))

    dir = 1
    for i in k:
        if i == 'R':
            dir *= -1
        elif i == 'D':
            try:
                if dir==1:
                    l.pop(0)
                else:
                    l.pop()
            except:
                print('error')
                break
    else:        
        if dir == 1:
            print('['+','.join(l)+']')
        else :
            l.reverse()
            print('['+','.join(l)+']')