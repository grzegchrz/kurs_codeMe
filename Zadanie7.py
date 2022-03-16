"""
Użyj pętli for, aby napisać program,
który będzie usuwał z jakiegoś przykładowego napisu wszystkie znaki specjalne, np. .,:;?!
"""
znaki = [".", ",", ":", ";", "?", "!"]
napis = input("Podaj napis -> ")
napisBezZnakow = ""
for literka in napis:
    if literka in znaki:
        b = napis.replace(literka, "")
    else:
        napisBezZnakow = napisBezZnakow + literka
print(napisBezZnakow)
