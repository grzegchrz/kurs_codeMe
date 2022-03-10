import random
def generatorHasel(dlugoscHasla):
    randomA = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    randomB = ['@', '#', '$', '=', ':', '?', '.', '/', '|', '~', '>', '*', '<']
    randomC = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    randomD = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',  'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    concatPassword = randomA + randomB + randomC + randomD
    password = "".join(random.sample(concatPassword, dlugoscHasla))
    print(password)

def main():
    dlugoscHasla = int(input("Program do generowania haseł. Podaj długości hasła >> "))
    wygenerujHaslo = generatorHasel(dlugoscHasla=dlugoscHasla)
    
main()