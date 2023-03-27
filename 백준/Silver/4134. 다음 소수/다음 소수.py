def isprime(k):
    if k==0 or k==1:
        return False
    for i in range(2,int(k**(1/2))+1):    
        if k%i==0:
            return False
    else:
        return True

for _ in range(int(input())):
    num = int(input())
    while True:
        if isprime(num) == True:
            print(num)
            break
        num +=1