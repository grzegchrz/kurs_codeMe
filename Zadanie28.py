import os.path

def szukaj(plik):
    if os.path.isfile(plik):
        print ("Plik istnieje")
        with open(plik) as f:
            contents = f.read()
            print(contents)
        exit()
    else:
        print ("Plik nie istnieje")
        exit(main())

def main():
    plik = input("Wprowadź nazwę pliku -- >")
    szukaj(plik=plik)
main()