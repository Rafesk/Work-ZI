a = 3
b = 3639868

def ibrel(a,b):
    a1 = b
    q = 0
    r = 10000000
    x1,x2,y1,y2 = 1,0,0,1
    x,y = 0, 0
    while(r > 1):
        q = a // b
        r = a % b
        x = x1 - q * x2
        y = y1 - q * y2
        x1, y1 = x2, y2
        x2, y2 = x, y
        a = b
        b = r
    obrEL = abs(x2) % a1
    return obrEL
#print(ibrel)
