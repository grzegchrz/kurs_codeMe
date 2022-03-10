def podzielNapis(napis):
    l = napis.split('-')
    chars = list(l)
    sortChars = sorted(chars)
    joinedString = "-".join(sortChars)
    print(joinedString)


def main():
    napis = input("Wprowadź sekwecję napisów rozdzieloną zakiem - np. kot-pies-albatros-czapla-delfin >> ")
    nowyNapis = podzielNapis(napis=napis)
main()