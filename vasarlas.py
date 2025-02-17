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

def egymasUtanKoltesNelkuliNap(sorok):
    KoltesNelkuliNapokSoroatba = 1
    KoltesNelkuliNapokSoroatbaOsszes = 0
    for i in range(len(sorok)):
        nap = sorok[i]
        if nap == '0':
            if nap == sorok[i-1]:
                KoltesNelkuliNapokSoroatba += 1
                if KoltesNelkuliNapokSoroatbaOsszes < KoltesNelkuliNapokSoroatba:
                    KoltesNelkuliNapokSoroatbaOsszes = KoltesNelkuliNapokSoroatba 
            else:
                KoltesNelkuliNapokSoroatba = 1
    return KoltesNelkuliNapokSoroatbaOsszes

szamok = Szambeolv(sor)
VNN = vasarlasNelkuliNapok(sor)
KNNS = egymasUtanKoltesNelkuliNap(sor)
print(sor)
print(VNN,"nap nem költött semmit.")
print("Átlag: ",sum(szamok)/len(szamok))
print("Legkisebb szám: ",min(szamok))
print("Legnagyobb szám: ",max(szamok))
print("Összes költés: ",sum(szamok))
print(KNNS, "napig sorozatba nem költött semmit.")
