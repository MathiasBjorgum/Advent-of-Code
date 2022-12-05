import sys
sys.path.append(".")

from data.data_util import get_data

def main():
    data = [(el[int(len(el)/2):], el[:int(len(el)/2)]) for el in get_data().split("\n")]

    common = [''.join(set(el[0]).intersection(el[1])) for el in data]

    sum_ = sum([(ord(el)-96) if el.islower() else (ord(el)-38) for el in common])

    print("Part 1:")
    print(sum_)

    data = [el for el in get_data().split("\n")]
    groups = [(data[el], data[el+1], data[el+2]) for i, el in enumerate(range(0, len(data), 3))]

    common = [''.join(set(el[0]).intersection(set(el[1])).intersection(set(el[2]))) for el in groups]

    sum_ = sum([(ord(el)-96) if el.islower() else (ord(el)-38) for el in common])
    
    
    print("Part 2:")
    print(sum_)
    

if __name__ == "__main__":
    main()