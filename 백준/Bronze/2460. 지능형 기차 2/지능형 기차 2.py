max = 0
p =0
for i in range(10):
    a,b= map(int,input().split())
    p = p+b-a
    if p>max:
        max = p
print(max)