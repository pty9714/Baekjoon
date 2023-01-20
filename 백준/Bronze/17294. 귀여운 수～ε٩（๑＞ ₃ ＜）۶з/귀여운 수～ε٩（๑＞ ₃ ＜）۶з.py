a = input()
for i in range(len(a)-1):
    if int(a[1])-int(a[0]) != int(a[i+1])-int(a[i]):
        print('흥칫뿡!! <(￣ ﹌ ￣)>')
        break
else:
    print('◝(⑅•ᴗ•⑅)◜..°♡ 뀌요미!!')