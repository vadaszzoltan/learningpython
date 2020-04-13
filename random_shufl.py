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

lista = ["ko", "papir", "ollo"]

jatekos = input('Válassz:')
jatekosvalasz = atalakitszobolszam(jatekos)
gep = random.choice(lista)
print ("Gepvalasz:"+gep)
gepvalasz = atalakitszobolszam(gep)
print (jatekosvalasz - gepvalasz)

