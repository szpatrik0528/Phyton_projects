import random
f= open("Órai munka\\ige.txt","r",encoding="utf-8")
a1= f.readline()
f.close()
f= open("Órai munka\\melleknev.txt","r",encoding="utf-8")
a2= f.readline()
f.close()
f= open("Órai munka\\mgh.txt","r",encoding="utf-8")
a3= f.readline()
f.close()
ige=a1.split(" ")
mell=a2.split(" ")
mgh=a3.split(" ")
nev=input("ki? ")
hol=input("hol? ")
ig=ige[random.randint(0,len(ige)-1)]
m1=mell[random.randint(0,len(mell)-1)]
m2=mell[random.randint(0,len(mell)-1)]
print(m1, nev, ige, m2, hol)