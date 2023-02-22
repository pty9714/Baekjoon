dic = {'A': 4,'B':3, 'C':2 , 'D':1, '+':0.5, '0': 0}
l = ['P','F',]
sum = 0
t = 0
for _ in range(20):
    a,b,c = input().split()
    if c == 'P':
        continue
    elif c == 'F':
        t += float(b)
    else:
        x,y= c
        sum+=(dic[x]+dic[y])*float(b)
        t += float(b)

print(round(sum/t,6))
