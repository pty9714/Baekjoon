
def fibo(n):
    if n<=1:
        return n
    else:
        cnt = 1
        a=0
        b=1
        while cnt !=n:
            a,b = b, a+b
            cnt +=1

        return b
    

print(fibo(int(input())))