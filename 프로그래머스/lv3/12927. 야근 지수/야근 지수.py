
def solution(n, works):
    answer = 0
    if sum(works)<=n:
        return answer
    works.sort()
    p = len(works)-1
    for i in range(n):
        works[p]-=1
        if works[p]<works[p-1]:
            p -= 1
        else:
            p = len(works)-1


    for i in works:
        answer += i**2
    return answer