def make_dict_code():
    d = {}
    with open("codes_braille.txt","r") as codes :
        for line in codes:
            if line.find("\n") != -1:
                t = line[:line.find("\n")].split(" ")
            else:
                t = line.split(" ")
            d[t[-1]] = t[0]
    codes.close()
    return(d)

def remplir():
    text_code = open("Braille.txt","w")
    while True :
        code = input("entrer le code :")
        if test(code):
            text_code.write(code)
            ask = input("tu peux ajouter un autre code Y/N ? :")
            if ask !="Y":
                break
            else:
                text_code.write("\n")
    text_code.close()
    
def test(code):
    if len(code) % 6==0:
        if set(code) == {"*","-"}:
            return(True)
        else:
            return(False)
    else :
        return(False)

def convertir(dict_code):
    res = ""
    with open("Braille.txt","r") as text_code:
        for line in text_code.read().split("\n"):
                for i in range((len(line)//6)):
                    code = line[6*i:6*(i+1)]
                    print(code,"code")
                    res += dict_code[code]
                res+= " "
                
                
    text_code.close()
    print(res)
            
            
dict_code = make_dict_code()
print(dict_code)
remplir()
convertir(dict_code)

"""
print(code,res)
"""
