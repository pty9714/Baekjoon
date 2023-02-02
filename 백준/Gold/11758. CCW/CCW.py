def ccw(x1, y1, x2, y2, x3, y3):
    a = x1 * y2 + x2 * y3 + x3 * y1
    b = y1 * x2 + y2 * x3 + y3 * x1
    if a - b> 0:
        return 1
    elif a==b:
        return 0
    else:
        return -1
        
x1,y1 = map(int,input().split())
x2,y2 = map(int,input().split())
x3,y3 = map(int,input().split())
print(ccw(x1,y1,x2,y2,x3,y3))
