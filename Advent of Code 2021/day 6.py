import os
from dataclasses import dataclass
import numpy as np
from collections import Counter
import random


def find_groups(data: list[int]):
    fish_count = {}
    for i in range(9):
        fish_count[i] = 0

    for el in data:
        fish_count[el] += 1
    
    return fish_count

def total_count_fish_dict(fishs: dict):
    returning = 0
    for value in fishs.values():
        returning += value

    return returning

def age_fish(fishs: dict):
    aged_fishs = {}

    for i in range(1, 9):
        aged_fishs[i-1] = fishs[i]

    aged_fishs[8] = fishs[0]
    aged_fishs[6] += fishs[0]


    return aged_fishs


def main():

    os.chdir("C:\\Users\\mathi\\OneDrive - NTNU\\Personlig\\Div kode\\Advent of Code 2021")

    with open("day_6_input.txt", 'r') as f:
        data = f.read().rstrip()


    data = [int(x) for x in data.split(',')]

    groups = find_groups(data)

    max_time = 256

    total_fish = groups
    for i in range(max_time):
        total_fish = age_fish(total_fish)

    print(total_count_fish_dict(total_fish))

if __name__ == "__main__":
    main()

