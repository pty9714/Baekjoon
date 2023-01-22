def recursion(s, l, r, k):
    if l >= r: return 1,k+1
    elif s[l] != s[r]: return 0,k+1
    else: return recursion(s, l+1, r-1,k+1)

def isPalindrome(s):
    k=0
    return recursion(s, 0, len(s)-1,k)

for i in range(int(input())):
    print(*isPalindrome(input()))