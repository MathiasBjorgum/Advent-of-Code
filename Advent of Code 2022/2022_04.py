import sys
from dataclasses import dataclass

from data.data_util import get_data

sys.path.append(".")


class Elf():

    def __init__(self, area):
        self.area_start, self.area_stop = area.split("-")

    def __repr__(self):
        return (f"start: {self.area_start}. stop: {self.area_stop}")

@dataclass
class Elfs():
    elfs: list[Elf]

    def check_contains(self):
        elf_area_1 = list(range(int(self.elfs[0].area_start), int(self.elfs[0].area_stop) + 1))
        elf_area_2 = list(range(int(self.elfs[1].area_start), int(self.elfs[1].area_stop) + 1))

        if set(elf_area_1).issubset(set(elf_area_2)) or set(elf_area_2).issubset(elf_area_1):
            return 1

        return 0

    def check_overlap(self):

        elf_area_1 = list(range(int(self.elfs[0].area_start), int(self.elfs[0].area_stop) + 1))
        elf_area_2 = list(range(int(self.elfs[1].area_start), int(self.elfs[1].area_stop) + 1))

        if set(elf_area_1).intersection(set(elf_area_2)) or set(elf_area_2).intersection(elf_area_1):
            return 1

        return 0


def main():
    data = get_data().split("\n")

    data = [Elfs([Elf(e[0]), Elf(e[1])]) for e in [(el.split(",")) for el in data]]

    print("Part 1:")
    print(sum([elfs.check_contains() for elfs in data]))

    print("Part 2:")
    print(sum([elfs.check_overlap() for elfs in data]))


if __name__ == "__main__":
    main()
