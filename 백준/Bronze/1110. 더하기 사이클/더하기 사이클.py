count = 0
a = int(input())
c = a
while True:
    a = (a%10)*10 + (a//10 + a%10)%10
    count += 1
    if c==a:
        break

print(count)