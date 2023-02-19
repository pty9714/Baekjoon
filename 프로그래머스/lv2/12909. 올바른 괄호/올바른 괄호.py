def solution(s):
    stack = []
    for i in s:
        if i == '(':
            stack.append(s)
        else:
            try:
                stack.pop()
            except:
                return False

    if stack:
        return False
    else:
        return True
