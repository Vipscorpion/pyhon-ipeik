
notes = open("C:/Users/slahb/OneDrive/Bureau/ipeikinfo/notes.txt","a")

while True:
    note = float(input("entrer le note :"))
    notes.write(str(note))
    ask = input("tu peut ajoute un note (oui/non) ? :")
    notes.write("\n")
    if ask == "non":
        break

notes.close()
print("{:.2f}".format(19))

t =[0]
with open("C:/Users/slahb/OneDrive/Bureau/ipeikinfo/notes.txt","r") as notes:
    for line in notes:
        t.append("{:.2f}".format(float(line)))
print(t)
notes.close()
print(t)
s = 0
for i in t:
    s+=i
    
moy = s/len(t)
print(f'moy : {moy:d}')