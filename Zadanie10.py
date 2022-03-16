import random

slowa_list = ['Grzegorz', 'Kot Puszek', 'mysz', 'Pełna miska', 'rower', 'zapiecek']

slowo = random.choice(slowa_list)
podziel_slowo = list(slowo.strip(" "))
random.shuffle(podziel_slowo)
print(f"Odgadnij wyraźenie{podziel_slowo}")

while True:
    zagdnij_slowo = input("Czy wiesz jakie to słowo -> ")
    if zagdnij_slowo == slowo:
        print ("Ale numer, trafiony zatopiony. Gratulacje!!!!")
        break
    else:
        print ("Spróbuj jeszcze raz.")