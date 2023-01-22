def fib(n):
    if n==1 or n==2:
        return 1
    else:
        return fib(n-2) + fib(n-1)


def fibonacci(n):
    f = [0,1,1]
    k=0
    for i in range(3,n+1):
        k+=1
        f.append(f[i-1] + f[i-2])
    return f[n],k


a = int(input())
print(fibonacci(a)[0],fibonacci(a)[1])