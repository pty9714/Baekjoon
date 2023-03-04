def solution(citations):
    a = max(citations)
    l = sorted(citations,reverse=True)
    for i in range(a,-1,-1):
        cnt = 0
        for j in l:
            if i<=j:
                cnt+=1
            else:
                break
        if cnt>=i:
            answer = i
            break
    return answer