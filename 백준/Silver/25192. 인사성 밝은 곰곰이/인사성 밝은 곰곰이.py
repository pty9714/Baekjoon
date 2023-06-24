n = int(input())
ans = 0
dic = {}
for i in range(n):
    str = input()
    if str == 'ENTER':
        ans += len(dic)
        dic = {}
    else:
        dic[str] = dic.get(str, 0) + 1
ans += len(dic)
print(ans)