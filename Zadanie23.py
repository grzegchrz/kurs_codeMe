
import re

def findDate(napis):
    s = napis
    pattern = r'\d{4}-\d{2}-\d{2}'
    dates = [("\n".join(re.findall(pattern,s)))]
    print(dates)


def main():
    napis = input("Wprowadź napis, w którym poszukamy daty w formacie YYYY-MM-DD. >> ")
    nowyNapis = findDate(napis=napis)
main()