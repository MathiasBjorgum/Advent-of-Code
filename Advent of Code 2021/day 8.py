import os
from dataclasses import dataclass

@dataclass
class Instruction:
    inputs: list[str]
    outputs: list[str]

    def total(self) -> list[str]:
        return self.inputs + self.outputs

    def __repr__(self) -> str:
        return f"in: {self.inputs}\n out: {self.outputs}"



def main():
    os.chdir("C:\\Users\\mathi\\OneDrive - NTNU\\Personlig\\Div kode\\Advent of Code 2021")

    data = []

    with open("day_8_input.txt", 'r') as f:
        tmp = f.readlines()

    # tmp = ["acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf"]
    
    for el in tmp:
        splitted = el.split("|")
        inputs = splitted[0].split()
        outputs = splitted[1].rstrip().split()
        data.append(Instruction(inputs, outputs))

    number_count = 0

    for inst in data:
        for out in inst.outputs:
            if   len(out) == 2: number_count += 1
            elif len(out) == 7: number_count += 1
            elif len(out) == 4: number_count += 1
            elif len(out) == 3: number_count += 1

    print(f"Part 1: {number_count}")

    # mapping = [set()] * 10

    total = 0
    for inst in data:
        mapping = [set()] * 10
        for inp in inst.total():
            if   len(inp) == 2: mapping[1] = set(inp)
            elif len(inp) == 4: mapping[4] = set(inp)   
            elif len(inp) == 3: mapping[7] = set(inp)
            elif len(inp) == 7: mapping[8] = set(inp)

    # for inst in data:
        for inp in inst.total():
            if len(inp) == 6:
                # Siden 1 og 6 har kun ett felleselement funker dette
                if len(mapping[1] - set(inp)) == 1:
                    mapping[6] = set(inp) 
    
    # for inst in data:
        for inp in inst.total():
            if len(inp) == 5:
                if len(mapping[1] - set(inp)) == 0:
                    mapping[3] = set(inp)
                elif len(set(inp) - mapping[6]) == 0:
                    mapping[5] = set(inp)
                elif len(set(inp) - mapping[6]) == 1:
                    mapping[2] = set(inp)
    
    # for inst in data:
        for inp in inst.total():
            if len(inp) == 6 and set(inp) not in mapping:
                if len(mapping[5] - set(inp)) == 0:
                    mapping[9] = set(inp)
                else:
                    mapping[0] = set(inp)

            
    
        s = ""
    # for inst in data:
        for inp in inst.outputs:
            s += str(mapping.index(set(inp.strip())))

        total += int(s)

    print(mapping)
    print(total)

    





if __name__ == "__main__":
    main()