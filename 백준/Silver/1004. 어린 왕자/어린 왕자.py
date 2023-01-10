
def include(a,b,c,d,e):
    if ((c-a)**2 + (d-b)**2)**(1/2) > e :
        return 0
    else:
        return 1

k = int(input())
for i in range(k): 
    dot = list(map(int,input().split()))
    count = 0
    num = int(input())
    for i in range(num):
        pl=list(map(int,input().split()))
        str_dot = include(dot[0],dot[1],pl[0],pl[1],pl[2])
        end_dot = include(dot[2],dot[3],pl[0],pl[1],pl[2])
        if str_dot==1 and end_dot==1:
            continue
        if str_dot == 1:
            count +=1
        if end_dot == 1:
            count +=1
    print(count)