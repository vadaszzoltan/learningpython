import random
print ('Ez egy kő / papír / olló játák')
jatekos = input('Válassz:')
lista = ["Kő", "Papír", "Olló"]
print ("A gép azt mondta, hogy: ", random.choice(lista)) 
print ('Te azt választottad, hogy:', (jatekos))