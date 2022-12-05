import sys
sys.path.append(".")

from data.data_util import get_data

def calculate_score(data):

    opponent = data[0]
    you = data[1]

    score = 0

    if opponent == "A" and you == "X": score = 1 + 3
    if opponent == "A" and you == "Y": score = 2 + 6
    if opponent == "A" and you == "Z": score = 3 + 0

    if opponent == "B" and you == "X": score = 1 + 0
    if opponent == "B" and you == "Y": score = 2 + 3
    if opponent == "B" and you == "Z": score = 3 + 6

    if opponent == "C" and you == "X": score = 1 + 6
    if opponent == "C" and you == "Y": score = 2 + 0
    if opponent == "C" and you == "Z": score = 3 + 3

    return score

def calculate_choice(data):

    opponent = data[0]
    outcome = data[1]

    choice = ""

    if opponent == "A" and outcome == "X": choice = "Z"
    if opponent == "A" and outcome == "Y": choice = "X"
    if opponent == "A" and outcome == "Z": choice = "Y"

    if opponent == "B" and outcome == "X": choice = "X"
    if opponent == "B" and outcome == "Y": choice = "Y"
    if opponent == "B" and outcome == "Z": choice = "Z"

    if opponent == "C" and outcome == "X": choice = "Y"
    if opponent == "C" and outcome == "Y": choice = "Z"
    if opponent == "C" and outcome == "Z": choice = "X"

    return choice



def main():
    data = get_data()

    data = [el.split() for el in data.split("\n")]

    print("Part 1:")
    print(sum([calculate_score(el) for el in data]))

    print("Part 2:")
    print(sum([calculate_score((el[0],calculate_choice(el))) for el in data]))

if __name__ == "__main__":
    main()