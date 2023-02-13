def solution(phone_book):
    phone_book = sorted(phone_book)
    p = len(phone_book)
    for i in range(p-1):
        t = min(len(phone_book[i]),len(phone_book[i+1]))
        for k in range(t):
            if phone_book[i][k] != phone_book[i+1][k]:
                break
        else:
            return False                   
    else:
        return True