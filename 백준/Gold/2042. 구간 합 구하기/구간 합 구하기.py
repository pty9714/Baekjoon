N,M,K = map(int,input().split())
def lsb(i):
    return int(bin(i&(~i+1)),2)

def lst_renewal(index,value):
    while True:
        global l2
        global N
        k = lsb(index)
        l2[index]+=value
        index = index + k
        if index>N:
            break

def psum(index):
    answer = 0
    while index != 0:
        answer +=l2[index]
        index-=lsb(index)
    return answer



l = [0]
l2 = [0 for _ in range(N+1)]

for i in range(N):
    l.append(int(input()))

for i in range(1,N+1):
    lst_renewal(i,l[i])
    # print(l2)

for _ in range(M+K):
    a,b,c = map(int,input().split())
    if a == 1:
        lst_renewal(b,c-l[b]) 
        l[b] = c
    else:
        print(psum(c)-psum(b-1))