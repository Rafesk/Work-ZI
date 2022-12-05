from modular_arithmetic import mulinv
p =  73 
a =  1 
b =  1

k = 0
for x in range(0,p):
    for y in range(0,p):
        Sright = (x**(3) + a*x + b) % p
        Sleft = (y**(2)) % p
        if(Sleft == Sright):
            k+=1
            print(f"K={k} (x,y) = ({x},{y})")


#x = [0,1] #[6,  2] [66,  4]
#y = [6,2] # [6,  2] [66, 69]
# 26 { 20,  8}
x1 = 21
x2 = 50
y1 = 31
y2 = 41

k11 = (y2-y1) % p
k22 = mulinv((x2-x1),p) 
lb1 = (k11 * k22) % p
# k1 = (x1*x1*3+a) % p 
# k2 = mulinv((2*y1),p)
# lb2 = (k1*k2) % p
lb = lb1
x3 = (lb*lb-x1-x2) % p
y3 = (lb*(x1-x3)-y1) % p
print(f"(x,y) = ({x3},{y3})")

# 2T = (21,31)
# 4T = (27,1)
# 8T = (20,65)
# 16T = (21,42)
# 24T = (50,41)
# 26T = (20,65)

# 3 задание (69,15)
# 4 task  (0,0)
# 5 task  (20,65)