
jelszo = 'Lajos'

bemenet = input('Mi a jelszo?')

proba = 0

while bemenet != jelszo:
    proba += 1
    if proba == 3: 
        print('A rendszer lezárt!')
        break
    print('A jelszo hibás, probáld újra!')
    bemenet = input('Mi a jelszo? ')

if bemenet == jelszo:
    print('Belépés engedélyezve a rendszerhez!')
    
