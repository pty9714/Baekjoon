a,b,c = map(int,input().split())
sec = int(input())
time = 3600*a+60*b+c+sec
print(f'{(time//3600)%24} {((time%3600)//60)%60} {(time%60)%60}')