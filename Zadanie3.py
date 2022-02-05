# take three values from user
val1 = input("Wprowadź tytuł ulubionej piosenki: ")

# Display all values on screen
print("\n")
print("wypisuje z ilu znaków się składa")
countLeter = len(val1)
print(countLeter)
print("wypisuje ile razy występuje literka a")
countLeterA = val1.count('a')
print(countLeterA)
print("wypisuje, czy w tytule występuje spacja")
checkSpacja = " "
if checkSpacja in val1:
    print("Spacja występuje w tytule")
else:
    print("Spacja nie występuje w tytule")
print("wypisuje tytuł ze wstawionymi znakami specjalnymi (np. #, * lub -) pomiędzy każdy znak tytułu")
val1ToList = list(val1)
napisSuper = "-".join(val1ToList)
print(napisSuper)
print(val1.replace("", "-"))
print("wypisuje tytuł z usuniętymi spacjami")
print(val1.replace(" ", ""))
