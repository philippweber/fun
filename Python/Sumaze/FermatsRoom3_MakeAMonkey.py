#Sqr,Cube,x2,x3,-2,-2,-2
#Sqr,Cube,x2,x3,-3,-3,-3

#s=sqr
#c=cube
#d=x2 (double)
#t=x3 (tripple)
#m=-2
#n=-3

#Shortest solutions:
#['t', 't', 'm', 'm', 'c', 'd', 'd']
#['t', 's', 'm', 'm', 'c', 'd', 'd']
#['n', 'm', 's', 's', 'n', 'n', 'd']
#['n', 'd', 's', 's', 'n', 'n', 'd']
#['n', 'c', 'd', 's', 'n', 'n', 'd']
#['m', 'n', 's', 's', 'n', 'n', 'd']

choices=['s','c','d','t','m','m','m','s','c','d','t','n','n','n']
steps=[]
start=1
calculations=0

def permutate(remaining,depth,value):
  global calculations
  global steps
  new_remaining=list(remaining)
  new_remaining.pop(0)
  for x in range(len(remaining)):
    y=remaining[x]
    steps.append(y)
    if(y=='s'):
      new_value=value*value
    elif(y=='c'):
      new_value=value*value*value
    elif(y=='d'):
      new_value=value*2
    elif(y=='t'):
      new_value=value*3
    elif(y=='m'):
      new_value=value-2
    elif(y=='n'):
      new_value=value-3
    else:
      print('What the fuck is this: '+y)
    calculations+=1
    #if(calculations%10000==0):
    if(calculations%1000000==0):
        print calculations
    if(new_value==500):
      print '500 found:'
      print steps
      exit()
    if((depth<13)and(value<1000)):
      permutate(new_remaining,depth+1,new_value)
    new_remaining.append(y)
    new_remaining.pop(0)
    steps.pop()

permutate(choices,0,start)


