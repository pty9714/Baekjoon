a = int(input())
list = []

for i in range(a):
    num1,num2 = map(int, input().split())
    list.append(num1+num2)


for i in range(a):
    print(list[i])