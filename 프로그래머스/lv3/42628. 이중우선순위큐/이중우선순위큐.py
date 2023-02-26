l = []
def solution(operations):
    for i in operations:
        if i[0] == 'I':
            l.append(int(i[2:]))
            l.sort()
        elif i == 'D 1':
            try:
                l.pop()
            except:
                continue
        else:
            try:
                l.pop(0)
            except:
                continue
        
    if l:
        answer = [max(l),min(l)]
    else:
        answer = [0,0]

    return answer
