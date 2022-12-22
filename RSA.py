from modular_arithmetic import mulinv

p = 1787
q = 2039  
text = 926526
n = p*q
yn = (p-1)*(q-1)
e = 3
d = mulinv(e,yn)
C = text**(e) % n
Mc = C**d % n
print("C=",C)
print("M=",Mc)
st = d %(p-1)
r1 = ((C**p) **st)% p
st = d % (q-1)
r2 = ((C%q)**st) % q
print(r1)
print(r2)