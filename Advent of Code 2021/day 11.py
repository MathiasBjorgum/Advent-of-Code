import os
import numpy as np
from dataclasses import dataclass

def blink(data):
    pass


def main():
    os.chdir("C:\\Users\\mathi\\OneDrive - NTNU\\Personlig\\Div kode\\Advent of Code 2021")

    d = [list(l.rstrip()) for l in open("day_11_input_tst.txt", 'r')]
    data = []
    data.append([0 for i in range(len(d[0])+2)])
    for el in d:
        el.insert(0, "0")
        el.append("0")
        data.append(list(map(int, el)))
    data.append([0 for i in range(len(d[0]))])
    
    for line in data:
        print(line)


if __name__ == "__main__":
    main()