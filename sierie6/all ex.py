print("ex1")

def binaire(n):
    if n//2 == 0:
        return str(n%2)
    else:
        return str(binaire(n//2))+str(n%2)

print(binaire(10))

"----------------------------------------------"
print("ex2")

def long(ch):
    if ch == "":
        return 0
    else:
        return 1+long(ch[1:])
    
long("hello")

"---------------------------------------------"
print("ex3")

def U(n):
    if n<2 :
        return 0
    else:
        return 3*U(n-1) + U(n-2)
    
print(U(3))

"------------------------------------------------"
print("ex4")

def palindrome(ch):
    if ch == "" or len(ch) == 1:
        return True
    if ch[0]==ch[-1]:
        return palindrome(ch[1:-1])
    else:
        return False

print(palindrome("aya"))

"-------------------------------------------------"
print("ex5")

def positive(l):
    if len(l)==1 :
        if l[0]>=0 :
            return True
        else:
            return(False)
    
    if l[0] >=0:
        return(positive(l[1:]))
    else:
        return(False)

print(positive([10]))

"---------------------------------------------------"
print("ex6")

def croissante(l):
    if len(l) == 1:
        return True
    if l[0]<=l[1]:
        return(croissante(l[1:]))
    else:
        return False
    
print(croissante([1,2,3,-1]))

'---------------------------------------------------'
    
print("ex7")


'---------------------------------------------------'

print("ex8")

def pgcd(a,b):
    if b == 0 or a == 0 or a==b :
        return max(a,b)
    elif max(a,b)%min(a,b) == 0:
        return(min(a,b))
    else:
        return pgcd(min(a,b),max(a,b)%min(a,b))

print(pgcd(11,121.0))
        
"---------------------------------------------------------"
print("ex9")

def taille(l):
    if len(l) == 0:
        return([("",0)])
    elif len(l) == 1:
        return[(l[0],len(l[0]))]
    else:
        return[(l[0],len(l[0]))]+taille(l[1:])

print(taille(["free"]))
