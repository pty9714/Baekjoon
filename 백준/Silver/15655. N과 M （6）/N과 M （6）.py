n, m = map(int,input().split())
lst = list(map(int,input().split()))
lst.sort()
l = []
check = [False]*n
def recur(num):
    if num == m:
        return print(*l)
    else:
        for i in range(n):
            if check[i] == False:
                for j in range(i+1):
                    check[j] = True
                l.append(lst[i])
                recur(num+1)
                for j in range(i+1):
                    check[j] = False
                l.pop()

recur(0)