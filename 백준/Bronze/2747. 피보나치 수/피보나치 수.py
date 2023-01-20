a= int(input())
i = 0
j = 1
while a!=1:
    k = j
    j += i
    i = k
    a -=1
print(j)
