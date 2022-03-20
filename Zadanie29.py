import os
import json
import time
from collections import OrderedDict
import pandas as pd


with open("songs.json", encoding="utf-8", newline="") as plik:
    dane = json.load(plik)

parent_dir = "C:/Users/grzeg/PycharmProjects/pythonProject1/"
directory = "piosenki"


path = os.path.join(parent_dir, directory)
os.mkdir(path)

artistList = []
print(dane)
for i in range(len(dane)):
    artistList.append(dane[i]['artist'])
print(len(artistList))

res = list(OrderedDict.fromkeys(artistList))
print(len(res))

root_path = "C:/Users/grzeg/PycharmProjects/pythonProject1/piosenki/"
for x in res:
    pathArtist = os.path.join(root_path, x)
    print(pathArtist)
    os.mkdir(pathArtist)

for y in range(len(dane)):
    artist = ((dane[y]['artist'])) + "/"
    title = ((dane[y]['title']))
    lyrics = ((dane[y]['lyrics']))

    _dir = os.path.join(root_path, artist)

    completeName = os.path.join(_dir, title + ".txt")
    print(completeName)
    file1 = open(completeName, "w")
    file1.write(lyrics)
    file1.close()



