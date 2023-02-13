def solution(genres, plays):
    d = {}
    answer = []
    igp = [] #(index,(genres,plays))
    for i in range(len(genres)):
        d[genres[i]] = d.get(genres[i],0)+plays[i]
        igp.append((i,(genres[i],plays[i])))
    l2 = sorted(d.items(),key = lambda x : -x[1])

    igp = sorted(igp,key = lambda x: x[1],reverse=True)
    for i in l2:
        cnt = 0
        for j in igp:
            if i[0]== j[1][0]:
                answer.append(j[0])
                cnt +=1
            if cnt==2:
                break
    return answer