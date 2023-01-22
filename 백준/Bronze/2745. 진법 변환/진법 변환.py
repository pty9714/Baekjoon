s,v = input().split()
s=s[::-1]
num = [chr(x) for x in range(ord('0'),ord('9')+1)]
UPP = [chr(x) for x in range(ord('A'),ord('Z')+1)]
total = 0
for i in range(len(s)): 
    if s[i] in num:
        total +=int(s[i])*(int(v)**i)
    else:
        total += (ord(s[i]) - ord('A') +10)*(int(v)**i)
print(total)