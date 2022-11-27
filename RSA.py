from modular_arithmetic import gcd_extended,mulinv

def RSA(p,q,text):
    n = p*q
    yn = (p-1)*(q-1)
    e = 3
    d = mulinv(e,yn)
    C = text**(e) % n
    Mc = C**d % n
    print("C=",C)
    print("M=",Mc)

p = 1787 #2339 
q = 2039 #1709 
text = 926526 #1142599 
RSA(p,q,text)