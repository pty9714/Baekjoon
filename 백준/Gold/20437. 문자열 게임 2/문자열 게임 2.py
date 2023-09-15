TC = int(input())
for _ in range(TC):
    t = input()
    n = len(t)
    m = int(input())
    set = {}
    l = [[] for _ in range(27)]
    for i in range(n):
        l[ord(t[i]) - ord('a')].append(i)

    answer = -1
    answer2 = 9999999999999
    for i in l:
        if len(i)>=m:
            for j in range(len(i)+1-m):
                answer2 = min(answer2,i[m-1+j]-i[j]+1)
                answer = max(answer,i[m-1+j]-i[j]+1)

    if answer != -1 and answer2 != 9999999999999:
        print(answer2, answer)
    else:
        print(-1)