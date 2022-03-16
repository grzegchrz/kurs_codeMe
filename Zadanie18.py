def pobliczSaldo(transakcje):
    suma = 0
    l = transakcje.split(';')
    desired_array = [int(numeric_string) for numeric_string in l]
    for s in desired_array:
        suma = suma + s
    print(f"Suma wynosi {suma}")


def main():
    transakcje = input("Wprowadź sekwecję trasakcji rozdzieloną zakiem ; np. 1000; -400; 200; 1500; -500 -> ")

    pobliczSaldo(transakcje=transakcje)

main()
