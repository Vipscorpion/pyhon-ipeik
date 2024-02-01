
def countFreq(f1,f2):
    with open(f1,"r") as F1 , open(f2,"w") as F2 :
        cont = F1.read()
        e = set(cont)-{"\n"}
        F2.write("{}".format({ x:cont.count(x) for x in e}))
    F1.close()
    F2.close()

# pg principale
f1 = "f1.txt"
f2 = "f2.txt"
countFreq(f1,f2)

"""
ch = "programme"
e = set(ch)
d = {x: ch.count(x) for x in e }

print(d, set("hello\nhi\nfree")-{"\n","h"} )
"""
