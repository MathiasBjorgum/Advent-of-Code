from io import StringIO
import os
from typing import Counter
import numpy as np
from dataclasses import dataclass

@dataclass
class Rule:
    inp: str
    out: str

    def __repr__(self) -> str:
        return f"I: {self.inp}. O: {self.out}"

def insert(polymer: list[str], rule_dict: dict):
    returning = []
    returning.append(polymer[0])
    for i in range(0, len(polymer)-1):
        pair = polymer[i] + polymer[i+1]
        # print(pair)
        # returning.append(polymer[i])
        if (pair in rule_dict.keys()):
            returning.append(rule_dict[pair])
        returning.append(polymer[i+1])

    return returning

def run(polymer: list[str], rule_dict: dict, no_runs: int):

    new_poly = polymer
    for i in range(no_runs):
        print(f"Run no: {i}")
        new_poly1 = insert(new_poly, rule_dict)
        new_poly = new_poly1
    
    counter = Counter(new_poly)
    return counter

def main():
    filepath = (os.getcwd())
    polymer = []
    rules = []
    rule_dict = {}
    with open(os.path.join(filepath,"day_14_input_tst.txt"), "r") as f:
        tmp = f.readlines()
        polymer = [ch for ch in tmp[0].rstrip()]
        for i in range(2, len(tmp)):
            split = tmp[i].split("->")
            # print(split)
            rule_dict[split[0].strip()] = split[1].strip()
            # rules.append(Rule(split[0].strip(), split[1].strip()))


    res = (run(polymer, rule_dict,10))
    res_max = (max(res.values()))
    res_min = min(res.values())
    print(f"max-min = {res_max} - {res_min} = {res_max-res_min}")

    '''
    Ide: Kun holde styr på antallet av hver bokstav
    '''



if __name__ == "__main__":
    main()