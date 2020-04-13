import random

def atalakitszobolszam(szo):
    if szo == 'ko':
        return 1
    if szo == 'papir':
        return 2
    if szo == 'ollo':
        return 3

def atalakitszambolszo(szam):
    if szam == 1:
        return "ko"
    if szam == 2:
        return "papir"
    if szam == 3:
        return "ollo"
def kiertekeles(eredmeny):
    if eredmeny == -1:
        return "vesztettel"
    if eredmeny == 1:
        return "nyertel"
    if eredmeny == -2:
        return "nyertel"
    if eredmeny == 2:
        return "vesztettel"
    if eredmeny == 0:
        return "dontetlen"

lista1 = ["ko", "papir", "ollo"]
lista2 = ["ko", "papir", "ollo"]

gep1valasz = random.choice(lista1)
print ("Elsőgép: "+gep1valasz)
gep2valasz = random.choice(lista2)
print ("Masikgép: "+gep2valasz)
gepvalasz1 = atalakitszobolszam(gep1valasz)
gepvalasz2 = atalakitszobolszam(gep2valasz)
vegeredmeny = (gepvalasz1 - gepvalasz2)
print (vegeredmeny)
eredmeny = vegeredmeny
print (kiertekeles(eredmeny))