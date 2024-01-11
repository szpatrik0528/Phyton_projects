def Magas_E(atlagmagassag):
    if atlagmagassag < 170:
        return False
    else:
        return True

név = input("Mi a tanuló neve:")
while(név!=""):
    magassag = int(input("Magasság: "))
    if Magas_E(magassag):
        print(név, "Magassabb mint az átlag!")
    else:
        print(név, "Nem magassabb mint az átlag!")
    név =input("Név:")    