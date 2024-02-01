
def concat(f1,f2,f3):
    try:
        with open(f1,"r") as F1 , open(f2,"r") as F2,open(f3,"w") as F3:
            cont = F1.read() + F2.read()
            F3.write(cont)
            
        F1.close()
        F2.close()
        F3.close()
            
        return(0)
    
    except FileNotFoundError :
        return(1)

# pg principale

f1 = "f1.txt"
f2 = "f2.txt"
f3 = "f3.txt"

print(concat(f1,f2,f3))




