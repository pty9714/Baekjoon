def solution(money):
    num = len(money)
    dp1 = [0] * (num-1)
    dp1[0] = money[0]
    for i in range(1, num-1):
        dp1[i] = max(dp1[i-1],dp1[i-2]+money[i])
    dp2 = [0] * num
    for i in range(1, num):
        dp2[i] = max(dp2[i-1],dp2[i-2]+money[i])
    answer = max(dp1[num-2],dp2[num-1])
    return answer