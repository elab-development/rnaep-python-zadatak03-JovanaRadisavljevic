import random
import math

proizvodi = ["Kamasne", "Cepin", "Karabiner", "Ranac", "Sator", "Stapovi za planinarenje", "Planinarske cipele", "Vodootporna jakna", "Termos", "Kompas"]
cene = {
    "Kamasne": 45.99,
    "Cepin": 89.50,
    "Karabiner": 12.99,
    "Ranac": 120.00,
    "Sator": 249.99,
    "Stapovi za planinarenje": 67.00,
    "Planinarske cipele": 159.90,
    "Vodootporna jakna": 199.99,
    "Termos": 25.50,
    "Kompas": 35.00
}
for proizvod,cena in cene.items():
    print(f'{proizvod} - {cena} €')

budzet = float(input("Unesite vas budzet: "))
for proizvod,cena in cene.items():
    if cena <= budzet:
        print(proizvod)

def najskuplji_proizvod():
    najskuplji = max(cene, key=cene.get)
    return najskuplji
print(f'najskuplji proizvod: {najskuplji_proizvod()}')

izabrani_proizvod = random.choice(proizvodi) 
print(f"Korisniku je privukao paznju proizvod: {izabrani_proizvod}")

prosek = math.floor(sum(cene.values()) / len(cene) * 100) / 100
print(f"Prosecna cena proizvoda: {prosek} €")

prodate_kolicine = [8, 3, 15, 12, 5, 10, 7, 4, 20, 6]
ukupan_prihod = 0
for i in range(len(proizvodi)):
    ukupan_prihod += cene[proizvodi[i]] * prodate_kolicine[i]
print(f"Ukupan prihod: {round(ukupan_prihod, 2)} €")

proizvodi.append("Vreca za spavanje")
cene["Vreca za spavanje"] = 49.99
prodate_kolicine.append(5)
print(proizvodi)

sortirani = sorted((cene[p], p) for p in proizvodi)
for c,p in sortirani:
    print(f'{p} - {c} €')