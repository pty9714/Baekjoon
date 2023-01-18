a, b = map(int,input().split())
d31 = [1,3,5,7,8,10,12]
d30 = [4,6,9,11]
total = 0
def day(m):
    if m in d31:
        return 31
    elif m in d30:
        return 30
    elif m == 2:
        return 28
    
for i in range(1,a):
    total += day(i)

total += b
answer = ['SUN','MON','TUE','WED','THU','FRI','SAT']
print(answer[total%7])