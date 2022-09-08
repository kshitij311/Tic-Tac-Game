n=int(input('Enter the number of player:'))
def board(y):
 print(y[0]+'|'+y[1]+'|'+y[2])
 print('------')
 print(y[3]+'|'+y[4]+'|'+y[5])
 print('------')
 print(y[6]+'|'+y[7]+'|'+y[8])
if n==2:
  y=[' ',' ',' ',' ',' ',' ',' ',' ',' ']
  board(y)
  d=0
  e='X'
  k=0
  p=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
  while True:
    if d==0 and k<9:
      c=int(input('Enter the position number:'))
      if k%2==0 and y[c-1]==' ':
        y[c-1]='X'
        e='X'
        board(y)
        k=k+1
      elif y[c-1]==' ':
        y[c-1]='O'
        e="O"
        board(y)
        k+=1
      else:
        print('Space already occupied')
      for i in p:
        if y[i[0]]==e and y[i[1]]==e and y[i[2]]==e:
          d+=1
    elif d==1:
      print(e+" won the game")
      break
    else:
      print('Tie')
      break
if n==1:
  y=[' ',' ',' ',' ',' ',' ',' ',' ',' ']
  board(y)
  d=0
  e='X'
  p=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
  x=[1,2,3,4,5,6,7,8,9]
  k=0
  while True:
    if d==0 and k<9:
      if k%2==0 :
        c=int(input('Enter the position number:'))
        if y[c-1]==' ':
         y[c-1]='X'
         e='X'
         board(y)
         x.remove(c)
         k+=1
        else:
         print('space already occupied')
      else:
        y[x[0]-1]='O'
        x.remove(x[0])
        e='O'
        board(y)
        k+=1
      for i in p:
        if y[i[0]]==e and y[i[1]]==e and y[i[2]]==e:
          d+=1
    elif d==1:
        print(e+" won the game")
        break
    else:
        print('Tie')
        break
