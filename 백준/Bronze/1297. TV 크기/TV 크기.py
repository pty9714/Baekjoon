a,b,c= map(int,input().split())
t = a/((b**2+c**2)**(1/2))
print (int(b*t) , int(c*t))