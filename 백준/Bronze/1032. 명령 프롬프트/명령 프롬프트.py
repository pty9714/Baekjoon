a = int(input())
k = list(input())
for i in range(a-1):
    ct = list(input())
    for j in range(len(ct)):
        if k[j] != ct[j]:
            k[j] = '?'

print(''.join(k))
