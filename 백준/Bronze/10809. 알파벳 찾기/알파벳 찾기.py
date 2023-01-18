#10809
dict = {} 
for i in range(ord('a'),ord('z')+1):
    dict[chr(i)] = -1 # dict에 {'a':-1, 'b':-1 ..., 'z':-1} 입력

a = list(input())
count = 0 # 몇번째에 등장하는지 세는 자리수
for i in a:
    if dict[i] == -1:
        dict[i] = count # dict에 -1 대신 자리수를 입력
        count +=1
    else:
        count +=1 # 중복된 알파벳이 있는경우 입력하지않고 다음 자리
for i in dict:
    print(dict[i],end=' ')