#Расширенный алгоритм Евклида
def gcd_extended(num1, num2):
    if num1 == 0:
        return (num2, 0, 1)
    else:
        div, x, y = gcd_extended(num2 % num1, num1)
    return (div, y - (num2 // num1) * x, x)
#обратный элемент
def mulinv(a, b):
    g, x, y = gcd_extended(a,b)
    #print(f'Делитель равен {g}, x = {x}, y = {y}')
    if g == 1:
        return x % b
    else:
        return 0
a = 5
b = 7
#print(mulinv(a,b))