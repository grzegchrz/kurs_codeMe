cenaBenzyny = 6
srednieSpalanie = 8
val1 = int(input("Wprowadź cenę za przejazd: "))
val2 = int(input("Wprowadź ilość kilometrów do przejechania: "))

tripCena = ((val2)/8)*cenaBenzyny
print(tripCena)

if tripCena > val1:
    print("Musisz zatankować po drodze")
else:
    print("Spokojnie dojedziesz")