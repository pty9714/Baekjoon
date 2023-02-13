def solution(participant, completion):
    participant = sorted(participant)
    completion = sorted(completion)
    for i in range(len(completion)):
        a = participant.pop()
        b = completion.pop()
        if a!=b:
            answer = a
            break
    else:
        answer = participant[0]
    return answer