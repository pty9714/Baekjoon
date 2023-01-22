s = input()
l = []
i = 0
while i != len(s):
    if s[i] == ' ':
        print(*l[::-1],sep='',end=' ')
        l = []
        i +=1
        continue
    elif s[i] == '<':
        print(*l[::-1],sep='',end='')
        l = []
        while s[i] !='>':
            l.append(s[i])
            i+=1
        print(*l,sep='',end='')
        print('>',end='')  
        i+=1
        l=[]
        continue
    elif i == len(s)-1:
        try:
            l.append(s[i])
            print(*l[::-1],sep='',end='')
            break
        except:
            break
    l.append(s[i])
    i+=1
