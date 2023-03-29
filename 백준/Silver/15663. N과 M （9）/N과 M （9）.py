n, m = map(int,input().split())
lst = list(map(int,input().split()))
lst.sort()
l = []
check = [False]*n
def recur(num):
    if num == m:
        return print(*l)
    else:
        prev = 0
        for i in range(n):
            if check[i] == False and prev != lst[i]:
                check[i] = True
                prev = lst[i]
                l.append(lst[i])
                recur(num+1)
                check[i] = False
                l.pop()

recur(0)