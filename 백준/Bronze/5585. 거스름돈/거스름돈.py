a = int(input())
a = 1000 - a
l = [500,100,50,10,5,1]

total = 0
for i in l:
    if a>=i:
        total+=a//i
        a%=i
print(total)