import json

with open("songs.json", encoding="utf-8", newline="") as plik:
    dane = json.load(plik)

def most_frequent(List):
    return max(set(List), key=List.count)

artistList = []

for i in range(len(dane)):
    artistList.append(dane[i]['artist'])

print(most_frequent(artistList))


