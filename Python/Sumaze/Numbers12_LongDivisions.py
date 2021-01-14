# ((n%70)==16) ((n%45)==11) ((n%65)==19) ((n%80)==7)  ((n%60)==17)
# ((n%13)==9)  ((n%5)==2)   ((n%2)==1)   ((n%50)==37) ((n%50)==27)
# ((n%30)==27) ((n%2)==0)   ((n%11)==3)  ((n%40)==27) ((n%3)==1)

def printtable(n, table):
  print('Number: '+str(n))
  for ri, row in enumerate(table):
    for ci, col in enumerate(row):
      if col:
        print('x', end='')
      else:
        print(' ', end='')
      #print(str(ri)+','+str(ci)+':'+str(col))
    print('')

def hop(n, table, rp, cp):
  rn = rp+1
  if rn == len(table):
    printtable(n, table)
    return
  # Go down
  if table[rn][cp]:
    hop(n, table, rn, cp)
  # Go right
  for ci in range(cp+1,len(table[rp])):
    if table[rp][ci]:
      if table[rn][ci]:
        hop(n, table, rn, ci)
    else:
      break
  # Go left
  for ci in range(cp-1,-1,-1):
    if table[rp][ci]:
      if table[rn][ci]:
        hop(n, table, rn, ci)
    else:
      break

for n in range(0, 1001):
  #print('Number '+str(n))
  table = [ [ ((n%70)==16), ((n%45)==11), ((n%65)==19), ((n%80)==7),  ((n%60)==17) ],
          [ ((n%13)==9),  ((n%5)==2),   ((n%2)==1),   ((n%50)==37), ((n%50)==27) ],
           [ ((n%30)==27), ((n%2)==0),   ((n%11)==3),  ((n%40)==27), ((n%3)==1)   ] ]
  # Find starting point
  for ci in range(0, len(table[0])):
    if table[0][ci] and table[1][ci]:
      hop(n, table, 1, ci) 

