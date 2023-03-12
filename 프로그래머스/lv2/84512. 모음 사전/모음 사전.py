l = ['','A','E','I','O','U']
t = []
t = set(t)
for j in l:
    for k in l:
        for q in l:
            for p in l:
                for w in l:
                    t.add((j+k+q+p+w).strip())
t = list(t)
t.sort()

def solution(word):
    for i in t:
        if i == word:
            return t.index(i)