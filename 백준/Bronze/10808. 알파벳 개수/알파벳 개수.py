string = input()
l = [0]*26
for i in string:
    l[ord(i)-ord('a')]+=1
print(*l)