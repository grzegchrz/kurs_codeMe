"""
- 10% dla osób poniżej 20 roku życia, 15% dla osób powyżej 70 roku życia
- rodzina pracowników - 12% przy cenie poniżej 3000, 20% przy cenie równej lub powyżej 3000 zł
- punkty z programu lojalnościowego: 10 zł za każde 100 punktów
Stwórz dwa warianty programu.
Wariant 1 programu zakłada, że aplikujemy wszystkie przysługujące zniżki,
wariant 2 programu zakłada, że wybieramy tę najkorzystniejszą
"""
cenaTelefonu = int(input("Podaj kwotę na telefon -> "))
wiek = int(input("Podaj swój wiek -> "))
rodzinaPracownika = input("Czy jesteś rodziną pracownika (tak/nie) -> ")
liczbaPunktowLojalnosciowych = int(input("Podaj liczbę punktów lojalnościowych -> "))

discount20 = 0.10
discount70 = 0.15
familyLess3k = 0.12
familyMore3k = 0.20
pionts100 = 10
howManyPoints = 100

discountPricePhone= 0
print(f"Zdeklarowan kwota na telefon {cenaTelefonu}")

if rodzinaPracownika == "tak":
    if cenaTelefonu >= 3000:
        discountPricePhone = cenaTelefonu * familyMore3k
    elif cenaTelefonu < 3000:
        discountPricePhone = cenaTelefonu * familyLess3k
else:
    discountPricePhone
print(f"Zniżka z tytułu Rodziny {discountPricePhone}")

disscountAge = 0

if wiek >= 70:
    disscountAge = cenaTelefonu * discount20
elif wiek <= 20:
    disscountAge = cenaTelefonu * discount70
else:
    disscountAge
print(f"Zniżka z tytułu wieku {disscountAge}")


discountPoints = 0
countPoints = liczbaPunktowLojalnosciowych / howManyPoints
discountPoints = round(countPoints) * pionts100
liczbaPunktowLojalnosciowych = 0
print(f"Zniżka z tytułu punktów lolajnościowych {discountPoints}")

"Wariant 1"
wariant1Cena = cenaTelefonu - discountPricePhone - disscountAge - discountPoints
print(f"Cena telefonu po przyznaniu wszystkich zniżek {wariant1Cena}")
"Wariant 2"
znizki = [discountPricePhone, disscountAge, discountPoints]
maxZnizka = max(znizki)
wariant2Cena = cenaTelefonu - maxZnizka
print(f"Cena telefonu po uzyskaniu najkorzystniejszej zniżki {wariant2Cena}")


