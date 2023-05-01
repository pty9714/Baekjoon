
def solution(numbers, target):
    cnt = 0
    stack = [(0,0)]
    while stack:
        s,l = stack.pop()
        if l>len(numbers):
            continue
        if l==len(numbers) and target == s:
            cnt +=1
        stack.append((s+numbers[l-1],l+1))
        stack.append((s-numbers[l-1],l+1))
        
    return cnt