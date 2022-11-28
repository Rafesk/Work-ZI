from math import gcd


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

def XOR(num1,num2):
    if(len(num1)!=len(num2)):
        prefix = (num1 if len(num1)>len(num2) else num2)[:(abs(len(num1)-len(num2)))]
    else:
        prefix = ""
    num3 =""
    for i in range(min(len(num1),len(num2))):
        if(num1[len(num1)-1-i] == num2[len(num2)-1-i]):
            num3 = num3 + "0"
        else:
            num3 = num3 + "1"
    out = prefix + num3[::-1]
    while(out[0]=="0" and ("1" in out )):
        out = out[1:len(out)]
    return out


def subbyte(num1, num2):
    n = num2
    r= delit(num1,num2)[0]
    q = delit(num1,num2)[1]
    x1,x2,y1,y2= 1,0,0,1
    x = XOR(str(ymnoz(q,x2)),str(x1))
    y = XOR(str(ymnoz(q,y2)),str(y1))
    while(True):
        r= str(delit(num1,num2)[0])
        q = delit(num1,num2)[1]
        x = XOR(str(ymnoz(q,x2)),str(x1))
        y = XOR(str(ymnoz(q,y2)),str(y1))
        x1,y1 =x2,y2
        x2,y2 = x,y
        num1 = num2
        num2 = r
        if(r=="1" or r=="0"):
            break
    return r,x,y, delit(x,n)[0]

a = "1101100111011010011110111110101000011010001100011101100010101011"
# 3 - 1101011000001111
b = "1110001010100010"
# 3 - 0101010111110011
sub = subbyte(a,b)
print(f"Обратный элемент = {sub[3]}, x = {sub[1]}, y = {sub[2]}, r = {sub[0]}")

#4 задание
step1 = subbyte(a,b)[3] # a - byte, m(x) - b
print("step1 = ",step1)
a_="00011111"
step2 = ymnoz(step1, a_) 
print("step2 = ",step2)
m2 = "100000001"
step2_ = delit(step2,m2)[0]
print("step2_ = ",step2_)
b_ = "01101001"
step3 = XOR(step2_,b_)# Сейча тут XOR , если просто сложение, просто поменять на "+""
print("step3 = ",step3)
step3_ = delit(step3,m2)[0]
print("step3_ = ",step3_)
