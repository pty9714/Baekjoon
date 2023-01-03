a = int(input())
list = []
list_num1 = []
list_num2 = []

for i in range(a):
    num1,num2 = map(int, input().split())
    list_num1.append(num1)
    list_num2.append(num2)
    list.append(num1+num2)


for i in range(a):
    print(f'Case #{i+1}: {list_num1[i]} + {list_num2[i]} = {list[i]}')