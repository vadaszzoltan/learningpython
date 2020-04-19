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
        return "kettes gep nyert"
    if eredmeny == 1:
        return "egyes gep nyert"
    if eredmeny == -2:
        return "egyes gep nyert"
    if eredmeny == 2:
        return "kettes gep nyert"
    if eredmeny == 0:
        return "dontetlen"

lista = ["ko", "papir", "ollo"]
valaszok = []
x = 0
y = 0
z = 0
for i in range(10):
    gep1valasz = random.choice(lista)
    print ("Elsőgép: "+gep1valasz)
    valaszok.append(gep1valasz)
    gep2valasz = random.choice(lista)
    print ("Masikgép: "+gep2valasz)
    valaszok.append(gep2valasz)
    gepvalasz1 = atalakitszobolszam(gep1valasz)
    gepvalasz2 = atalakitszobolszam(gep2valasz)
    eredmeny = (gepvalasz1 - gepvalasz2)
    print (eredmeny)
    if eredmeny == -1:
        y = y + 1 #kettes gép nyert
    if eredmeny == 1:
        x = x + 1 #egyes gép nyert 
        valaszok.append(gep1valasz) #a jóválaszokat hozzáadjuk egy listáhozz
    if eredmeny == -2:
        x = x + 1 #egyes gép nyert
        valaszok.append(gep1valasz) #a jóválaszokat hozzáadjuk egy listáhozz
    if eredmeny == 2:
        y = y + 1 #kettes gép nyert
    if eredmeny == 0:
        z = z + 1 #döntetlen
    print (kiertekeles(eredmeny))
print (x)
print (y)
print (z)
print (valaszok)
print ("----------------------------új játék-----------------------")
x = 0
y = 0
z = 0
for i in range(1000):
    gep1valasz = random.choice(valaszok)
    print ("Elsőgép: "+gep1valasz)
    valaszok.append(gep1valasz)
    gep2valasz = random.choice(lista)
    print ("Masikgép: "+gep2valasz)
    valaszok.append(gep2valasz)
    gepvalasz1 = atalakitszobolszam(gep1valasz)
    gepvalasz2 = atalakitszobolszam(gep2valasz)
    eredmeny = (gepvalasz1 - gepvalasz2)
    print (eredmeny)
    if eredmeny == -1:
        y = y + 1 #kettes gép nyert
    if eredmeny == 1:
        x = x + 1 #egyes gép nyert 
        valaszok.append(gep1valasz) #a jóválaszokat hozzáadjuk egy listáhozz
    if eredmeny == -2:
        x = x + 1 #egyes gép nyert
        valaszok.append(gep1valasz) #a jóválaszokat hozzáadjuk egy listáhozz
    if eredmeny == 2:
        y = y + 1 #kettes gép nyert
    if eredmeny == 0:
        z = z + 1 #döntetlen
    print (kiertekeles(eredmeny))
print (x)
print (y)
print (z)
print (valaszok)