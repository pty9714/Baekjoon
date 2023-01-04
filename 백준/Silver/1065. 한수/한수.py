a = int(input())
i = 100
count=0
if a < 100:
    print(a)
if a >=100:
    while i<=a:
        if (((i//100)-((i%100)//10))==(((i%100)//10)-(i%10))):
            count +=1
        i += 1
    print (count+99)
    