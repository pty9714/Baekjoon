l = input()
happy = 0
sad = 0
for i in range(len(l)):
    try:
      if l[i] == ':' and l[i+1] == '-':
        if l[i+2] == ')':
          happy +=1
        elif l[i+2] =='(':
          sad +=1
    except:
      break

if happy == 0 and sad == 0:
  print('none')
elif happy>sad:
  print('happy')
elif happy<sad:
  print('sad')
else:
  print('unsure')