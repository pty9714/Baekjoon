C = int(input())
for _ in range(C) :
    students = list(map(int, input().split()))
    N = students[0]; score_list = students[1:]
    aver = sum(score_list) / N
    num_high = 0
    for item in score_list :
        if item > aver :
            num_high += 1
    perct = num_high / N
    print(f'{perct*100:.3f}%')