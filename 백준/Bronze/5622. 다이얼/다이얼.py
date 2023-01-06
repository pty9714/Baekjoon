
i = input().lower()
sum = 0
for a in i:
    if a =='a' or a=='b' or a=='c':
        sum +=3
    elif a=='d' or a=='e' or a=='f':
        sum +=4
    elif a=='g' or a=='h' or a=='i':
        sum +=5
    elif a=='j' or a=='k' or a=='l':
        sum +=6
    elif a=='m' or a=='n' or a=='o':
        sum +=7
    elif a=='p' or a=='q' or a=='r' or a=='s':
        sum +=8
    elif a=='t' or a=='u' or a=='v':
        sum +=9
    else :
        sum +=10

print(sum)