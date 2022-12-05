import sys
sys.path.append(".")
from dataclasses import dataclass

from data.data_util import get_data

@dataclass
class Elf():
    cal_list: list[int]

    def get_cal_count(self):
        return sum(self.cal_list)

def main():

    data = get_data()    

    elf_list: list[Elf] = []

    cal_list = []
    for el in data.split("\n"):
        
        if el == "":
            elf_list.append(Elf(cal_list))
            cal_list = []
        else:
            cal_list.append(int(el))
    elf_list.append(Elf(cal_list))

    print("Part 1")
    print(max([elf.get_cal_count() for elf in elf_list]))

    print("Part 2")
    print(sum(sorted([elf.get_cal_count() for elf in elf_list], reverse=True)[:3]))


if __name__ == "__main__":
    main()