import os
from inspect import stack
from pathlib import Path

DATA_PATH = Path(
    r"C:\Users\mathi\OneDrive - NTNU\Personlig\Div kode\Advent of Code\Advent of Code 2022\data")


def get_data(test_data: bool = False):

    filename = os.path.splitext(os.path.basename(stack()[1].filename))[0]

    if test_data:
        filename = filename + "_test"

    filename = filename + ".txt"

    with open(DATA_PATH / filename, "r") as f:
        return f.read()

def create_text_files():
    os.chdir(DATA_PATH)

    for i in range(2,26):
        print(str(i).zfill(2))
        with open(f"2022_{str(i).zfill(2)}_test.txt", "w") as f:
            pass
        with open(f"2022_{str(i).zfill(2)}.txt", "w") as f:
            pass