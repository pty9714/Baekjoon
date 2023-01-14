a = int(input())
l1 = list(map(int,input().split()))
l1_dic = {}
for i in l1:
    if i not in l1_dic:
        l1_dic[i] = 1
    elif i in l1_dic:
        l1_dic[i] += 1

b = int(input())
l2 = list(map(int,input().split()))
result = []
for i in l2:
    if i in l1_dic:
        result.append(l1_dic[i])
    else:
        result.append('0')
print (*result)