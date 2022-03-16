wyraz = str(input("Zagrajmy w grę. Podaj wyraz:  "))
wyraz = wyraz.lower()

slownik = {'a': 5, 'ą':10, 'b': 3, 'c': 1, 'ć':77, 'd': 4, 'e': 1, 'ę': 47, 'f': 1, 'g': 15, 'h': 1, 'i': 1, 'j': 9, 'k': 1, 'l': 1, 'ł':58,
           'm': 1, 'n': 1, 'ń':62,'o': 4, 'ó':82, 'p': 1, 'q': 9, 'r': 9, 's': 1, 'ś': 47, 't': 1, 'u': 1, 'v': 8, 'w': 1, 'x': 1,
           'y': 1, 'z': 1, 'ź':77, 'ż':105}


def obliczPunkty(wyraz) -> int:
    punkty = 0
    for literka in wyraz:
        if literka not in slownik:
            punkty += 100
            print(f"Wow użyłeś słowa z dziwnym znakiem. Brawo. Dostajesz 100 punktów")
        else:
            punkty += slownik[literka]
    return punkty


sumaPunkty = obliczPunkty(wyraz)
print(f"Słowo \"{wyraz}\" zawiera {sumaPunkty} punktów")