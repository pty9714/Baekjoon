def solution(numbers):
    answer = ''
    ans = list(map(str, numbers))
    ans = sorted(ans, key = lambda x: x*3, reverse = True) 
    answer = str(int("".join(ans)))
    return answer

