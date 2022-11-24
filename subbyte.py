
#a = [1,1,0,1,1,0,0,1,1,1,0,1,1,0,1,0,0,1,1,1,1,0,1,1,1,1,1,0,1,0,1,0,0,0,0,1,1,0,1,0,0,0,1,1,0,0,0,1,1,1,0,1,1,0,0,0,1,0,1,0,1,0,1,1]
#b = [1,1,1,0,0,0,1,0,1,0,1,0,0,0,1,0]
#enumerate(a): 

#деление многочлена [] -лист
def delit(a,b):
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
    return r, q

#перестановка чисел и добавление ещё одного элемента из a        
def perenos(abs, k):
    for i in range(1, len(abs)):
        abs[i-1]=abs[i]
    abs[len(abs)-1] = k
    return abs

#умножение многочлена ""  -строка
def ymnoz(a,b):
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
    
    b = b[:len(b)-2]
    for i in range(len(b)):
        if(b[len(b)-1]=="1"):
            k2 = "0"*(len(b)-3-i)+a+"0"*(i+2)
        else:
            k2 = "0"*(len(a)+len(b)-1)
        k1 = bin(int(str(k1),2) ^ int(str(k2),2))[2:]    
    return k1

#x = x1-q*x2
#y = y1 -q*y2
#[] - лист
def subbyte(a,b):
    a1 = b 
    r = a[0:len(b)]
    q = [0]
    r1 = []
    x1, x2 = "1", "0"
    y1, y2 = "0", "1"
    x,y = "0","0"
    while(len(r) != 1): # основной цикл алгоритма Эйлера
        while(a[0]==0):
            a.pop(0)
        while(b[0]==0):
            b.pop(0)    
        if(len(a)<len(b)):
            q = [0]
            r = a
        else:
            r1 = r
            r, q = delit(a,b)
        q1 = list(map(str, q))
        q1 = "".join(q1)
        x = int(str(x1),2) ^ int(ymnoz(q1,x2),2)
        y = int(str(y1),2) ^ int(ymnoz(q1,y2),2)
        x1, y1 = x2, y2
        x2, y2 = bin(x)[2:], bin(y)[2:]
        #print(bin(x)[2:],bin(y)[2:]) #последние x и y
        if(1 not in r):
            break
        while(r[0]==0):
            r.pop(0)
        a = b
        b = r
    if(1 not in r):
        return "не существует"
    else:
        obrEl = bin(int(x1,2) % int("".join(list(map(str,a1))),2))[2:]
        return obrEl

#x*a+y*b=1
astart = "1101011000001111" 
bstart = "0101010111110011"
a = [int(i) for i in astart] #делает из строки лист
b = [int(i) for i in bstart]

#нахождение обратного элемента
#print("Обратный элемент = ",(int(subbyte(a,b),2)*a % b)

#деление многочленов
r,q = delit(a,b)
r = "".join(list(map(str, r))) #делает из листа строку
q = "".join(list(map(str, q)))
print("Остаток = ", r," Целое = ",q)

#4 задание
step1 = subbyte(a,b) # a - byte, m(x) - b
print("step1 = ",step1)
a_="00011111"
step2 = ymnoz(step1, a_) 
print("step2 = ",step2)
m2 = "100000001"
step3 = bin(int(step2,2) % int(m2,2))[2:]
print("step2_ = ",step3)
b_ = "01101001"
step4 = bin(int(step3, 2) ^ int(b_, 2))[2:] # Сейча тут XOR , если просто сложение, просто поменять на "+""
print("step3 = ",step4)
step5 = bin(int(step4,2) % int(m2,2))[2:]
print("step3_ = ",step5)