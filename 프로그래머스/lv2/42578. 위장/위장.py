def solution(clothes):
    d = {}
    answer = 1
    for i in clothes:
        d[i[1]] = d.get(i[1],1)+1
    for value in d.values():
        answer *=value
    return answer-1