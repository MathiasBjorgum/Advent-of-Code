import os
import numpy as np
from dataclasses import dataclass

ALLOWED_CHARS = ["()", "[]", "{}", "<>"]
CHAR_MAP = {"(": ")", "[": "]", "{": "}", "<": ">"}
ERR_POINTS = {")": 3, "]": 57, "}": 1197, ">": 25137}

def convert(s):
    str1 = ""

    return(str1.join(s))

def check_corrupted(array):
    err_score = []
    for chunk in array:
        found = []
        for c in chunk:
            if c not in CHAR_MAP.values():
                found.append(c)
            else:
                if c == CHAR_MAP[found[-1]]:
                    found.pop()
                else:
                    err_score.append(ERR_POINTS[c])
                    found = []
                    break
    return sum(err_score)


    # if not found:
    #     print(f"Could not find: {reversed_target}, pos = {pos}")

def remove_adjecent(liste: str):
    no_adjecent = [ch for ch in liste]
    # print(liste)
    for i, el in enumerate(liste):
        # found = False
        if i == len(liste):
            continue
        try:
            if liste[i+1] == CHAR_MAP[el]:
                no_adjecent.pop(i)
                no_adjecent.pop(i+1)
                break
        except:
            pass
    
    if len(liste) != len(convert(no_adjecent)):
        return (remove_adjecent(convert(no_adjecent)))
    return (convert(no_adjecent))

def remove_one_apart(liste: str):
    one_apart = [ch for ch in liste]
    # print(one_apart)
    for i, el in enumerate(liste):
        if i == len(liste) - 1:
            continue
        try:
            if liste[i+2] == CHAR_MAP[el]:
                one_apart.pop(i)
                one_apart.pop(i+1)
                break
        except:
            pass
    if len(liste) != len(convert(one_apart)):
        return remove_one_apart(convert(one_apart))

    return convert(one_apart)

def remove_two_apart(liste: str):
    two_apart = [ch for ch in liste]
    for i, el in enumerate(liste):
        if i == len(liste) - 2:
            continue
        try:
            if liste[i+3] == CHAR_MAP[el]:
                two_apart.remove(el)
                two_apart.remove(CHAR_MAP[el])
                break
        except:
            pass
    if len(liste) != len(convert(two_apart)):
        return remove_two_apart(convert(two_apart))
    return convert(two_apart)



def main():
    os.chdir("C:\\Users\\mathi\\OneDrive - NTNU\\Personlig\\Div kode\\Advent of Code 2021")

    data = np.array([l.rstrip() for l in open("day_10_input.txt", 'r')])
    data = [l.rstrip() for l in open("day_10_input.txt", 'r')]

    tst = []
    print(check_corrupted(data))
    '''
    print(data[0])
    t1 = (remove_adjecent(data[0]))
    print(remove_one_apart(t1))

    for i, el in enumerate(data):
        tst.append(remove_adjecent(el))

    fin = []
    for i, el in enumerate(tst):
        fin.append(remove_one_apart(el))
    
    tst = []
    for i, el in enumerate(fin):
        tst.append(remove_adjecent(el))
    '''
    # print(tst)


if __name__ == "__main__":
    main()