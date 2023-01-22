
s = input()
upp = [chr(x) for x in range(ord('A'),ord('Z')+1)]
low = [chr(x) for x in range(ord('a'),ord('z')+1)]
for i in s:
    if i in upp:
        print(chr((ord(i)-ord('A')-3)%26+ord('A')),end='')
    elif i in low:
        print(chr((ord(i)-ord('a')-3)%26+ord('a')),end='')
    else:
        print(i,end='')