import sys
input = sys.stdin.readline
num  = int(input())
element = 1
l2 = []
result = []
numberlist = []

for i in range(num):
    k = int(input())
    numberlist.append(k)


for a in numberlist:  
    if a <element:
        if a != l2[-1]:
            print ('NO')
            break
        else:
            l2.pop()
            result.append('-')
    else:
        while element !=a:
            l2.append(element)
            result.append('+')
            element+=1

        result.append('+')
        element+=1
        result.append('-')
else:
    print(*result,sep='\n')