def zmienNapis(napis, oldSing, newSing):
    newString = ''
    for x in napis:
        if x == oldSing:
            x = newSing
            newString += x
        else:
            newString += x
    print(newString)

    #print (newSing if x == oldSing else x for x in napis)

def main():
    napis = list(input("Wprowadź napis, który chcemy zmodyfikować >> "))
    oldSing = input("Wprowadź stary znak >> ")
    newSing = input("Wprowadź nowy znak >> ")
    nowyNapis = zmienNapis(napis=napis, oldSing=oldSing, newSing=newSing)
    #nowyNapis = zmienNapis(oldSing=oldSing)
    #nowyNapis = zmienNapis(newSing=newSing)
main()