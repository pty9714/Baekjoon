
a = list(input())
count = len(a)
for i in range(len(a)):
    if a[i] == '=':
        if a[i-1] == 'c' or a[i-1] == 's' or a[i-1] == 'z':
            count -=1
        if a[i-1] == 'z' and a[i-2] == 'd':
            count -=1
    if a[i] == '-':
        if a[i-1] == 'c' or a[i-1] == 'd' :
            count -=1
    if a[i] == 'j':
        if a[i-1] == 'l' or a[i-1] == 'n' :
            count -=1

print(count)