from collections import deque

def solution(prices):
    price_len = len(prices)
    p = deque(prices)
    answer = []
    while True:
        check = p.popleft()
        if not p:
            answer.append(0)
            break
        cnt = 0
        for i in p:
            if check<=i:
                cnt+=1
            else:
                cnt+=1
                answer.append(cnt)
                break
        else:
            answer.append(cnt)
    
    return answer