def saisie():
    while True:
        try :
            n  = int(input("entrer (0<N<=50) : "))
        except ValueError :
            print("Error d'entrée")
        else:
            if 0<n<=50:
                break
    return(n)
        
def remplir(L1,L2,n):
    for i in range(n):
        while True :
            try:
                L1[i] = int(input("L1["+str(i)+"]= "))
                L2[i] = int(input("L2["+str(i)+"]= "))
            except ValueError :
                print("Error d'entrée")
            else:
                if L1[i] != 0 and 0<=L2[i]<=1 :
                    break
    L1.reverse()

def affiche(L1,L2,C,n):
    for i in range(n):
        if L2[i] == 1:
            C.append(L1[i])
    
    C.sort()
    print(C)

#pg principale
n = saisie()
L1 = [0]*n
L2 = [0]*n
remplir(L1,L2,n)
C = list()
affiche(L1,L2,C,n)


