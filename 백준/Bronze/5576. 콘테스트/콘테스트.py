
import sys
input = sys.stdin.readline
w = []
k = []
for _ in range(10):
    w.append(int(input()))
for _ in range(10):
    k.append(int(input()))
w.sort()
k.sort()
w_sum = 0
k_sum = 0
for _ in range(3):
    w_sum += w.pop()
    k_sum += k.pop()
print(w_sum,k_sum)
