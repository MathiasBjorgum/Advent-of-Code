import os
import numpy as np
from dataclasses import dataclass






def main():
    os.chdir("C:\\Users\\mathi\\OneDrive - NTNU\\Personlig\\Div kode\\Advent of Code 2021")

    data = np.array([l.rstrip() for l in open("day_9_input_tst.txt", 'r')])

    minimums = []

    for row, line in enumerate(data):

        for col, num in enumerate(line):
            num = int(num)
            # Antar at num er er lavest
            low = True
            # Skjekker col > 0, og da mot nummeret til venstre
            if col > 0 and low:
                low = num < int(line[col-1])
            # Dersom skjekken over stemmer skjekker vi col < lengden, og mot den til høyre
            if col < len(line) - 1 and low:
                low = num < int(line[col+1])
            # Dersom skjekken over stemmer skjekker vi row > 0, og da mot nummeret over
            if row > 0 and low:
                low = num < int(data[row-1][col])
            # Dersom skjekken over stmmer skjekker vi row < len(data), og da mot nummeret under
            if row < len(data) - 1 and low:
                low = num < int(data[row+1][col])
            # Dersom skjekken over stemmer må vi ha et minimum
            if low:
                minimums.append(num)

    risk_level = 0
    for i in minimums:
        risk_level += 1 + i

    print(risk_level)

    








if __name__ == "__main__":
    main()




