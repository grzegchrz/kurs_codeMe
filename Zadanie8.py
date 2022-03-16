
# creating an empty list
lista = []

# iterating till the range
for i in range(0, 10):
    print(f"Wprowadź {i+1} element z 10 i naciśnij Enter")
    ele = int(input())

    lista.append(ele)  # adding the element

print(lista)

suma = 0

for s in lista:
    suma = suma + s
print(f"Suma wynosi {suma}")

srednia = (suma / len(lista))
print(f"Średnia wynosi {srednia}")

max = max(lista)
print(f"Wartość minimalna {max}")

min = min(lista)
print(f"Wartość minimalna {min}")