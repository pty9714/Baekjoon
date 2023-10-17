n,b = map(int,input().split())
l = []
for i in range(n):
    l.append(list(map(int,input().split())))


def matrix_mul(l1,l2):
    global n
    lst = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n): 
            for k in range(n):
                lst[i][j] += l1[k][j] * l2[i][k]
        
            lst[i][j] %= 1000
    return lst


def matrix_pow(lst,n):
    if n == 1:
        return lst
    else:
        l = matrix_pow(lst,n//2)
        if n %2 == 0:
            return matrix_mul(l,l)
        else:
            return matrix_mul(matrix_mul(l,l),lst)
        


answer = matrix_pow(l,b)

if b == 1:
    for i in range(n):
        for j in range(n):
            l[i][j] %= 1000
    
    for i in range(n):
        print(*l[i])
else:
        
    for i in range(n):
        print(*answer[i])