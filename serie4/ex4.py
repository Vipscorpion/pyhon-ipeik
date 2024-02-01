
D_Famille = {'eve':['tom','lea','luc','kim'],
             'tom':['isa','bob'],
             'lea':['ali'],
             'bob':['bea','tim'],
             'luc':['sam','jon','lou'],
             'sam':['ana','guy'],
             'guy':['ben']}
print("2)")
p = input("entrer le prénom(clé) :")
if p in D_Famille:
    print("l'ensemble des enfants de {} sont : {}".format(p,"/".join(D_Famille[p])))
else:
    print("{} n'est pas une clé du dictionnaire".format(p))

print("3)")
x = input("entrer le prenom(clé):")
ch = ""
if x in D_Famille:
    for i in D_Famille[x]:
        if i in D_Famille:
            print(i,ch)
            ch += "/".join(D_Famille[i])+"/"
else :
    print("{} n'est pas une clé du dictionnaire".format(x))

if ch =="":
    print("{} n'a pas de petits-enfents".format(x))
else :
    print("les petits enfants de {} sont : {}".format(x,ch))

print("4)")
y = input("entrer le prenom de l'enfant : ")
test = False
for key,value in D_Famille.items():
    if y in value:
        test = True
        print("Le parent de {} est {}".format(y,key))

if not(test):
    print("{} n'a pas de parent".format(y))

print("5)")
X = set()
while True:
    parent = input("enter a parent name : ")
    while not(parent in D_Famille):
        parent = input("enter a parent name : ")
    X.add(parent)
    ask = input("do you want to add a parent name (Y/N) ? : ")
    if ask == "N":
        break

enfant = set()
for f in X:
    enfant = enfant | set(D_Famille[f])

print("les enfant de {} sont : {}".format(X,enfant))
