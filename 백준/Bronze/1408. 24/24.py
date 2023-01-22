a,b,c= map(int,input().split(':'))
k = a*3600+b*60+c
a,b,c= map(int,input().split(':'))
t = a*3600+b*60+c -k
if t<0:
    t = 24*3600+t
print(f'{str(t//3600).zfill(2)}:{str((t%3600)//60).zfill(2)}:{str(t%60).zfill(2)}')