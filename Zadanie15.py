def liczenieZnakow(napis):
    print(napis)
    countUpper = 0
    countLower = 0
    for elem in napis:
        if elem.isupper():
            countUpper += 1
        elif elem.islower():
            countLower +=1
    print(f'W zdaniu występuje {countUpper} wielkich liter')
    print(f'W zdaniu występuje {countLower} małych liter')


def main():
    napis = input("Wprowadź zdanie w którym policzym i wypiszem liczbę małych i dużych liter w tym zdaniu >> ")
    policzenieZnakow = liczenieZnakow(napis=napis)
    
main()
