for _ in range(int(input())):
    num = int(input())
    l = [1,1,1,2,2] + [0]*(num-4)

    for i in range(5,num+1):
        l[i] = l[i-1] + l[i-5]

    print(l[num-1])