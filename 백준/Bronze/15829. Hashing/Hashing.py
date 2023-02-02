num = int(input())
s = input()
total = 0
for i in range(len(s)):
    total += (31**i)*(ord(s[i])-96)%1234567891
print(total)