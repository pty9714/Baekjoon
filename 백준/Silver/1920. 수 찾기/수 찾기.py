a=int(input())
l = list(map(int,input().split()))
dic = {}
for i in l:
    dic[i] = dic.get(i,1)
b = int(input())
l2 = list(map(int,input().split()))
for j in l2:
    k = dic.get(j,0)
    print(k)