n = int(input())
lst = list(map(int,input().split()))
rev_lst = list(reversed(lst))
lst_check = [1]*n
rev_lst_check = [1]*n

for i in range(n):
    for j in range(i):
        if lst[i]>lst[j]:
            lst_check[i] = max(lst_check[i],lst_check[j]+1)
        if rev_lst[i]>rev_lst[j]:
            rev_lst_check[i] = max(rev_lst_check[i],rev_lst_check[j]+1)

result = [0]*n
for i in range(n):
    result[i] = lst_check[i]+rev_lst_check[n-i-1]-1

print(max(result))