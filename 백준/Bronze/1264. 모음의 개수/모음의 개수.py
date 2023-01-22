l = ['a','e','i','o','u']
while True:
    s = input().lower()
    cnt = 0
    if s == '#':
        break
    else:
        for i in s:
            if i in l:
                cnt+=1
    print(cnt)