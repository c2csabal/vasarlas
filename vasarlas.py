f = open('vasarlas.csv','r', encoding='utf-8')
sor = (f.readline())
sor = sor.strip().split(';')
f.close

def vasarlasNelkuliNapok(sorok):
    napokSzama = 0
    vasarlasNelkuliNapok = 0
    szamok = []
    for szam in sorok:
        szamok.append(int(szam))
        napokSzama += 1
        if szam == '0':
            vasarlasNelkuliNapok += 1
    return vasarlasNelkuliNapok
    
VNN = vasarlasNelkuliNapok(sor)

print(sor)
print(VNN,"nap nem költött semmit.")
