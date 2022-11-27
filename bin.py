def perenos(abs, k):
    for i in range(1, len(abs)):
        abs[i-1]=abs[i]
    abs[len(abs)-1] = k
    return abs
def delit(a,b):
    if(a == b):
        return "0","1"
    a = [int(i) for i in a] #делает из строки лист
    b = [int(i) for i in b]
    while(a[0]==0 and (1 in a)):
        a.pop(0)
    while(b[0]==0 and (1 in b)):
        b.pop(0)
    r = a[0:len(b)]
    k = len(b)
    q = [0]
    
    
    while(k<len(a)):      
        check = 0
        while(r[0]==0):
            check += 1
            r = perenos(r,a[k])
            k += 1
            if(k==len(a)):
                break
        if(check>=2):
            for i in range(check-1):
                q.append(0)
        if(r[0]==1):
            q.append(1)
            #d1 = slogM(d1,b)
            for i in range(len(b)):
                if(b[i]==r[i]):
                    #print(0)
                    r[i]=0
                else:
                    r[i] = 1
    while(r[0]==0 and (1 in r)):
        r.pop(0)
    while(q[0]==0 and (1 in q)):
        q.pop(0)
    return "".join(list(map(str, r))), "".join(list(map(str, q)))
def ymnoz(a,b):
    a = str(a)
    b = str(b)
    if(a == "0" or b == "0"):
        return 0

    if(len(b)>len(a)):
        a,b = b,a

    if(len(b) == 1):
        if(b[0] == "1"):
            return a
        else:
            return "0"*len(a)
    
    if(b[len(b)-1] == "1"):
        k1 = "0"*(len(b)-1)+a
    else:
        k1 = "0"*(len(a)+len(b)-1)
    if(b[len(b)-2]=="1"):
        k2 = "0"*(len(b)-2)+a+"0"
    else:
        k2 = "0"*(len(a)+len(b)-1)
    if(len(b) == 2):
        return bin(int(str(k1),2) ^ int(str(k2),2))[2:]
    
    b = b[:len(b)-1]
    for i in range(len(b)):
        if(b[len(b)-1-i]=="1"):
            k2 = "0"*(len(b)-2-i)+a+"0"*(i+1)
        else:
            k2 = "0"*(len(a)+len(b)-1)
        k1 = bin(int(str(k1),2) ^ int(str(k2),2))[2:]    
    return k1


def gcd_extendedMN(num1, num2):
    print(num1,num2)
    if int(str(num2),2) == 0:
        return (num1, 0, 1)
    else:
        
        div, x, y = gcd_extendedMN(num2,delit(num1,num2)[0])
    return (div, bin(int(str(y),2) ^ int(str(ymnoz(delit(str(num1),str(num2))[1], x)),2))[2:], x)
print(delit("1010111","0010000"))
print(gcd_extendedMN("1010111","100011011"))
