import os
import numpy as np

def shortest_path(grid: np.ndarray):
    cost = 0
    visited_coord = []
    x = len(grid[0])
    y = len(grid)
    target = (x, y)
    target = (2,2)

    pass

def main():
    filepath = (os.getcwd())
    grid = []
    with open(os.path.join(filepath,"day_15_input_tst.txt"), "r") as f:
        for line in f.readlines():
            line = line.rstrip()
            appending = []
            for el in line:
                appending.append(int(el))
            grid.append(appending)

    grid = np.array(grid)
    
    print(grid)




if __name__ == "__main__":
    main()
