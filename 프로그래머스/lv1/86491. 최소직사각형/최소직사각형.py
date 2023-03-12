def solution(sizes):
    x=0; y=0
    for a,b in sizes:
        t1 = max(a,b)
        t2 = min(a,b)
        x = max(t1,x)
        y = max(t2,y)
    answer = x*y
    return answer