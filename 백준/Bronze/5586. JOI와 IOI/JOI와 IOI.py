a = input()
j =0
k =0
for i in range(0,len(a)-2):
    if a[i:i+3] == 'JOI':
        j +=1
    if a[i:i+3] == 'IOI':
        k +=1

print(j)
print(k)