a = input()
total = 0
for i in a:
    total +=int(i)
if ('0' in a) and (total%3 == 0):
    a = sorted(a,reverse=True)
    print(*a,sep='')
else: # 0이없다
    print('-1')