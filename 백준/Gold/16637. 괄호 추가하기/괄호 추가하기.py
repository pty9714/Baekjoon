n = int(input())
s = input()
answer = -2**31-1
def op(a,b,c):
    if b == "+":
        return int(a)+int(c)
    if b == "-":
        return int(a)-int(c)
    if b == "*":
        return int(a)*int(c)
    
def dfs(index,value):
    global answer
    if index == n-1:
        answer = max(answer,value)
    
    if index < n-2:
        dfs(index+2,op(value,s[index+1],s[index+2]))
    
    if index < n-4:
        dfs(index+4,op(value,s[index+1],op(s[index+2],s[index+3],s[index+4])))

dfs(0,int(s[0]))
print(answer)
