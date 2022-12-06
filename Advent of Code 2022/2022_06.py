from data.data_util import get_data
import sys
import time
sys.path.append(".")


def solve(data, n_unique):
    for i in range(n_unique, len(data)):
        sub = data[i-n_unique:i]

        if len(set(sub)) == len(sub):
            return i

    return 0


def main():
    data = get_data()

    # Function:
    start = time.time()
    print(solve(data, 4))
    print(solve(data, 14))
    end = time.time()
    print(end - start)

    # Comprehension
    start = time.time()
    print([i for i in range(4, len(data)) if len(
        set(data[i-4:i])) == len(data[i-4:i])][0])
    print([i for i in range(14, len(data)) if len(
        set(data[i-14:i])) == len(data[i-14:i])][0])
    end = time.time()
    print(end - start)


if __name__ == "__main__":
    main()
