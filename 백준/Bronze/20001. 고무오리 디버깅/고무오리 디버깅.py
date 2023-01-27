g = input()
a = ''
cnt = 0
while a != '고무오리 디버깅 끝':
    a = input()
    if a == '문제':
        cnt+=1
    elif a== '고무오리':
        if cnt>=1:
            cnt -=1
        else:
            cnt +=2

if cnt == 0:
    print('고무오리야 사랑해')
else:
    print('힝구')