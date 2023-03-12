from itertools import permutations
def solution(k, dungeons):
    nums = [i for i in range(len(dungeons))]
    perm = list(permutations(nums, len(dungeons)))
    answer = 0
    for i in perm:
        cnt = 0
        p = k
        for j in i:
            a,b = dungeons[j]
            if p>=a:
                p -= b
                cnt+=1
            else:
                answer = max(answer,cnt)
                break
        else:
            answer = max(answer,cnt)
    return answer