from winreg import QueryInfoKey


global key, text
text = "1aabefc9e901d7d3" #"ef8224d4d3e53497" 
#"9a0573bd4b2d295c"


key = ["d6c31d07","632628de","ecdbae99","6ffd7bfd","c58c398b","6ae57d79","c7982ec3","cd210f3a"]
#["df6a47bf" ,"efec06c5","22cb1c49", "eff6dca3", "afaab2ac","17025724","4cdbf718","82e00a7b"]
#["18a75dcf","2c1ee560","14621875","7206bfba","358ea8f4","e36ed553","18fb69db","0ec9b5b9"]


keyscelude = []#[["0"] * 8 for i in range(32)]
Sboxes = ["4a92d80e6b1c7f53","eb4c6dfa23810759","581da342efc7609b","7da1089fe46cb253","6c715fd84a9e03b2","4ba0721d36859cfe","db413f590ae7682c","1fd057a4923e6b8c"]
#["4a92d80e6b1c7f53","eb4c6dfa23810759","581da342efc7609b","7da1089fe46cb253","6c715fd84a9e03b2","4ba0721d36859cfe","db413f590ae7682c","1fd057a4923e6b8c"]


#создание большого ключа
def NewKey(keyscelude):
    k1 = 0
    for i in range(32):
        if(i<24):
            keyscelude.append(key[k1])
        else:
            keyscelude.append(key[7-k1])    
        k1 += 1
        if(k1==8):
            k1 = 0
    return keyscelude
keyscelude = NewKey(keyscelude)
#format(raund, "x") - 16 
#format(17, 'b') - двоичная
#int(keyscelude[0],16) - с 16 в десятичную

def WokrRaund(tl, tr,ik):#раунды
    raund = int(keyscelude[ik],16)
    k = format((int(tr,16)+raund) % (2**32),'x') # R+K mod 2^32  -- в 16-ой системе
    Sr = ""
    if(len(str(k)) != 8): # если в начале он убрал нули
        k = "0"*(8-len(str(k)))+k
    for i, step in enumerate(k): #перевод по S-boxes
        Sr += Sboxes[i][int(step,16)]
    SrDV = (format(int(Sr,16),'b')) #S(R) - двоичная
    SrDVMas =['0'] * 32
    for i in range(len(SrDV)): #запись в виде массива S(R)
        SrDVMas[len(SrDVMas)-1-i] = str(SrDV[len(SrDV)-1-i])
    SrDVMasSHIFT =['0'] * 32   
    for i in range(len(SrDVMas)):# алгоритм shift
        if(i<11):
            SrDVMasSHIFT[len(SrDVMasSHIFT)-1-10+i] = SrDVMas[i]
        else:
            SrDVMasSHIFT[i-10-1] = SrDVMas[i]
    #XOR
    tlDV = (format(int(tl,16),'b')) #Lr - двоичная
    tlDVMas =['0'] * 32
    for i in range(len(tlDV)): #запись в виде массива Lr
        tlDVMas[len(tlDVMas)-1-i] = tlDV[len(tlDV)-1-i]
    for i in range(len(tlDVMas)): #XOR
        if(tlDVMas[i]==SrDVMasSHIFT[i]):
            tlDVMas[i] = '0'
        else:
            tlDVMas[i] = '1'
    tl = tr
    tr = format(int(''.join(tlDVMas),2),'x')
    return tl, tr

tl = text[:len(text)//2] #левая часть
tr = text[(len(text)//2):len(text)] #правая часть

for i in range(len(keyscelude)):
    tl, tr = WokrRaund(tl,tr,i)

print("LC = ",tr)
print("RC = ",tl)