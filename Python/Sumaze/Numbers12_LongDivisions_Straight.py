for n in range(0, 1001):
    if ((n%70)==16) and ((n%13)==9) and ((n%30)==27):
        print("1 %d" % (n))
    if ((n%45)==11) and ((n%5)==2) and ((n%2)==0):
        print("2 %d" % (n))
    if ((n%65)==19) and ((n%2)==1) and ((n%11)==3):
        print("3 %d" % (n))
    if ((n%80)==7) and ((n%50)==37) and ((n%40)==27):
        print("4 %d" % (n))
    if ((n%60)==17) and ((n%50)==27) and ((n%3)==1):
        print("5 %d" % (n))

