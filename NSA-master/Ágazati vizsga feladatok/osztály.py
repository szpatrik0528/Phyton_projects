class Konyv:
    def __init__(self, cím, oldalszám, mufaj):
        self.cím = cím
        self.oldalszám = oldalszám
        self.mufaj = mufaj

t = []
for x in range(3):
    a = input("Add meg a könyv címét!: ")
    b = input("Add meg a könyv oldalszámát!: ")
    c = input("Add meg a könyv műfaját!: ")
    t.append(Konyv(a, b, c))
for x in range(3):
    print(t[x].cím,(""))