k = input()
answer = []
for i in range(1,len(k)-1):
    for j in range(i+1,len(k)):
        answer.append((k[i-1::-1])+(k[j-1:i-1:-1])+(k[-1:j-1:-1]))
answer.sort()
print(answer[0])