a= int(input())
x= int(input())
b= int(input())
y= int(input())
t= int(input())
if t>=45:
    print(a+(t-30)*x*21,b+(t-45)*y*21)
elif t>=30:
    print(a+(t-30)*x*21,b)
else:
    print(a,b)