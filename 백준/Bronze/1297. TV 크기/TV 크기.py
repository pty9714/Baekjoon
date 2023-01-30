a,b,c= map(int,input().split())
t = (b**2+c**2)**(1/2)
print (int(a*b/t) , int(a*c/t))