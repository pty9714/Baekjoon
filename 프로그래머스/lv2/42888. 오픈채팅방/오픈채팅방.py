def solution(record):
    lst = []
    dic = {}
    answer = []
    for s in record:
        if s[0] == 'E':
            e,id,nickname = s.split()
            lst.append((1,id))
            dic[id] = nickname
        elif s[0] == 'C':
            c,id,nickname = s.split()
            dic[id] = nickname
        else:
            l,id = s.split()
            lst.append((2,id))

    for i in lst:
        if i[0] == 1:
            t = dic[i[1]] + "님이 들어왔습니다."
            answer.append(t)
        else:
            t = dic[i[1]] + "님이 나갔습니다."
            answer.append(t)
    
    return answer

