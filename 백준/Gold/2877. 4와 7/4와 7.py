a = int(input())
b = format(a+1,'b')
print(str(b[1:]).replace('0','4').replace('1','7'))