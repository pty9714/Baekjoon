import math
for _ in range(int(input())):
  l = list(map(int,input().split()))
  total = 0
  for i in range(1,len(l)-1):
    for j in range(i+1,len(l)):
      total += math.gcd(l[i],l[j])

  print(total)