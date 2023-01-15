a = input()
k = []
for i in range(1,len(a)+1):
    for j in range((len(a)-i+1)):
        k.append((a[j:i+j]))

print(len(set(k)))
