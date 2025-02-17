f = open('vasarlas.csv','r', encoding='utf-8')
sor = (f.readline())
sor = sor.strip().split(';')
f.close

def Szambeolv(sorok):
    szamok = []
    for szam in sorok:
        szamok.append(int(szam))
    return szamok

def vasarlasNelkuliNapok(sorok):
    napokSzama = 0
    vasarlasNelkuliNapok = 0
    for szam in sorok:
        napokSzama += 1
        if szam == '0':
            vasarlasNelkuliNapok += 1
    return vasarlasNelkuliNapok
szamok = Szambeolv(sor)
VNN = vasarlasNelkuliNapok(sor)

print(sor)
print(VNN,"nap nem költött semmit.")
print("Átlag: ",sum(szamok)/len(szamok))
print("Legkisebb szám: ",min(szamok))
print("Legnagyobb szám: ",max(szamok))
print("Összes költés: ",sum(szamok))
