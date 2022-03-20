import random

def generujLiczby(zakres):
    l = zakres.split(',')
    desired_array = [int(numeric_string) for numeric_string in l]
    dolnyZakres = desired_array[0]
    gornyZakres = desired_array[1]
    ileLiczb = desired_array[2]
    for s in range(ileLiczb):
        print(random.randrange(dolnyZakres, gornyZakres))

def main():
    zakres = input("Wprowadź sekwecję trasakcji rozdzieloną zakiem , np. 1,20,5 -- >")
    generujLiczby(zakres=zakres)
main()