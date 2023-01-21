a = input()
total = 10
for i in range(len(a)-1):
    if a[i+1] == a[i]:
        total +=5
    else:
        total +=10
print(total)