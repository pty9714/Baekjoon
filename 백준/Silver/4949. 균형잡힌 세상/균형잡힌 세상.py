import sys
input = sys.stdin.readline
str = input().rstrip()
brk = ['(',')','[',']']

while str != '.':
    l = []
    for i in str:
        if i in brk:
            l.append(i)
    result = ''.join(l)
    temp = result.replace('()','')
    temp = temp.replace('[]','')
    while result!=temp:
        result = temp[:]
        temp = result.replace('()','')
        temp = temp.replace('[]','')
    if result:
        print('no')
    else:
        print('yes')

    str = input().rstrip()