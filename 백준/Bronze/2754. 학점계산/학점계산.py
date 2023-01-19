score = input()
if score[0] == 'F':
    print ('0.0')
else:
    s = 69-ord(score[0])
    if score[1] == '+':
        s+=0.3
    elif score[1] == '-':
        s-=0.3
    
    print(f'{s:.1f}')