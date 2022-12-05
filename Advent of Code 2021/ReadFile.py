import os

os.chdir("C:\\Users\\mathi\\OneDrive - NTNU\\Personlig\\Div kode\\Advent of Code 2021")

def getList(fileName: str) -> list:
    liste = []
    with open(fileName, "r") as f:
        for el in f.readlines():
            liste.append(el.rstrip())
        # liste.append(f.readlines())

    return liste

    