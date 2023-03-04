def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        x,y,z = commands[i]
        l = sorted(array[x-1:y])
        answer.append(l[z-1])
    return answer