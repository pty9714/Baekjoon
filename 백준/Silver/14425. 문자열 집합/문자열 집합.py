a,b = map(int,input().split())
l1 = []
count = 0
for i in range(a):
    l1.append(input())
for i in range(b):
    word = input()
    if word in l1:
        count +=1
print(count)