cenaBenzyny = 6
srednieSpalanie = 8
cenaZaPrzejazd = int(input("Wprowadź cenę za przejazd: "))
dlugoscTrasy = int(input("Wprowadź ilość kilometrów do przejechania: "))
cenaZa100km = 6*8

tripCena = ((dlugoscTrasy)/100*cenaZa100km)

if tripCena > cenaZaPrzejazd:
    print("Musisz zatankować po drodze")
else:
    print("Spokojnie dojedziesz")
