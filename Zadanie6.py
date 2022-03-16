wynikMeczu = input("Podaj wynik meczy np. 1:1 -> ")
lst = wynikMeczu.split(':')
val1 = int(lst[0])
val2 = int(lst[1])
if val1 > val2:
    res1 = val1 - val2
    print(f"Gospodarze strzelili o {res1} wiecej goli")
elif val1 < val2:
    res2 = val2 - val1
    print(f"Goście strzelili o {res2} wiecej goli")
elif val1 == val2:
    print("Padł Remis")