import random

def odczytaj_imiona(liczba):
    imiona = open('imiona')
    nazwiska = open('nazwiska')
    with open("imiona", newline="", encoding="utf-8") as plik:
        zawartoscImion = plik.read().split()
    #print(zawartoscImion)

    with open("nazwiska", newline="", encoding="utf-8") as plik:
        zawartoscNazwisk = plik.read().split()
    #print(zawartoscNazwisk)
    with open('generator', 'w') as f:
        for i in range(liczba):
            gen = (random.choice(zawartoscImion) + " " + random.choice(zawartoscNazwisk))
            f.write(gen)
            f.write('\n')

def main():
    liczba = int(input("Wprowadź liczbę generacji >> "))
    odczytaj_imiona(liczba=liczba)
main()




