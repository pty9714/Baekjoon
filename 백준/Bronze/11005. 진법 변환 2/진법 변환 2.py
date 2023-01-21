a,b = map(int,input().split())
l = [chr(x) for x in range(ord('A'),ord('Z')+1)]
c = ''
while a!=0:
    r = a%b
    if r<10:
        c= str(r)+c
    else:
        c = l[r-10]+c
    a = a//b

print(c)