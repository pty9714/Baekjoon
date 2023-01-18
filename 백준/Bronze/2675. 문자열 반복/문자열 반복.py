a = int(input())
for i in range(a):
    num, st = map(str,input().split())
    num = int(num)
    list1 = list(st)
    for i in list1:
        print(i*num,end='')
        
    print()