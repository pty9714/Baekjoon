k = 1000000
def fibo(n):
    global l
    if n<=1:
        return n
    else:
        cnt = 1
        a=0
        b=1
        while cnt !=n:
            a,b = b%k, (a+b)%k
            cnt +=1
        return b
    
t = int(input())
t =t%1500000
print(fibo(t))