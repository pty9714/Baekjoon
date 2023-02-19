def solution(progresses, speeds):
    answer = []
    while progresses:
        num = len(progresses)
        for i in range(num):
            progresses[i] += speeds[i]
        
        cnt = 0
        for i in range(num):
            if progresses[i]>=100:
                cnt+=1
            else:
                break
        for i in range(cnt):
            progresses.pop(0)
            speeds.pop(0)

        if cnt != 0 :
            answer.append(cnt)
        

    return answer