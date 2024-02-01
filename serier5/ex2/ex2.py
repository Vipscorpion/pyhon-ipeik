with open("f1.txt","r") as f1 , open("f2.txt","w") as f2 :
    for line in f1 :
        f2.write("{} {}".format(len(line.split(" ")) , line))
        
f1.close()
f2.close()
