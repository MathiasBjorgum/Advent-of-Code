import os



def get_fuel_use(pos: int, crabs: list[int]):
    fuel_use = 0

    for crab in crabs:
        fuel_use += ((pos - crab) **2 + (abs(pos - crab)))/2

    return fuel_use

def find_min_fuel(crabs: list[int]):

    current_min = 10000000000000000000
    for i in range(max(crabs)):
        if get_fuel_use(i, crabs) < current_min:
            current_min = get_fuel_use(i, crabs)

    return current_min

def main():
    os.chdir("C:\\Users\\mathi\\OneDrive - NTNU\\Personlig\\Div kode\\Advent of Code 2021")

    with open("day_7_input.txt", 'r') as f:
        data = [int (x) for x in f.read().split(',')]

    # data = [int(x) for x in "16,1,2,0,4,2,7,1,2,14".split(",") ]

    # print(data)
    # get_fuel_use(5, data)
    # print(get_fuel_use(1, data))
    # print(get_cost_of_move(2))
    print(find_min_fuel(data))





















if __name__ == "__main__":
    main()

