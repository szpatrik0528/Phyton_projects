import random 

class Szere:
    def __init__(self, név, foglalkozás, nem ,szám):
        self.név = név
        self.foglalkozás = foglalkozás
        self.nem = nem
        self.szám = szám

    def Fvn(a):
        if nem == "f":
            return "férfi"
        elif nem == "n":
            return "nő"

t = []
for x in range (3):
    a = input("Add meg a nevet!")
    b = input("Add meg a foglalkozást!")
    c = input("Add meg a nemet (f/n)!")
    d = random.randit(1,50)
    t.append(Szere(a,b,c,d))
for x in range (3):
    print(t[x].név,"")
    