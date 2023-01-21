a = int(input())
for i in range(a-1,-1,-1):
    print('*'*(a-i)+' '*(2*i)+'*'*(a-i))
for i in range(1,a):
    print('*'*(a-i)+' '*(2*i)+'*'*(a-i)) 