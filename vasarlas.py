f = open('vasarlas.csv','r', encoding='utf-8')

napokSzama = 0
vasarlasNelkuliNapok = 0
sor = (f.readline())
szamok = []
sor = sor.strip().split(';')
for szam in sor:
    szamok.append(int(szam))
    napokSzama += 1
    if szam == 0:
        vasarlasNelkuliNapok += 1

f.close
print(sor)
print("Átlag: ",sum(szamok)/len(szamok))
print("Legkisebb szám: ",min(szamok))
print("Legnagyobb szám: ",max(szamok))
print("Összes költés: ",sum(szamok))
print(vasarlasNelkuliNapok,"nap nem költött semmit.")
print(napokSzama,"napos volt a hónap")