import os
import numpy as np

def find_dimension(dots: list[tuple[int, int]]):
    max_x = 0
    max_y = 0
    for el in dots:
        if el[0] > max_x: max_x = el[0]
        if el[1] > max_y: max_y = el[1]
    
    return (max_x, max_y)


def convert_dots(fold: tuple[str, int], dots: set[tuple[int,int]]):
    dir = fold[0]
    axis = fold[1]
    dimensions = find_dimension(dots)
    # print(dimensions)
    # print(len(set(dots)))


    new_dots = []

    for dot in dots:
        appending_dot = []
        if dir == "y":
            appending_dot.append(dot[0])
            if dot[1] > axis:
                # print(axis - (axis - dot[0]))
                appending_dot.append(axis - (axis - dot[1]))
            else:
                appending_dot.append(dot[1])
            
            # appending_dot.append(dot[1])

        elif dir == "x":
            pass

        new_dots.append(tuple(appending_dot))


    print(len(set(new_dots)))

    # print(new_dots)



def main():
    filepath = (os.getcwd())
    dots = []
    folds = []
    with open(os.path.join(filepath,"day_13_input_tst.txt"), "r") as f:
        tmp = f.readlines()
        for i, el in enumerate(tmp):
            if el == "\n":
                for j in range(i+1, len(tmp)):
                    # folds.append(tmp[j].rstrip())
                    element = tmp[j].rstrip()[-3:]
                    axis = int(element[2])
                    direction = element[0]
                    folds.append((direction, axis))
                    # folds.append(element)
                break
            else:
                dots.append(eval(el.rstrip()))

    print(dots)
    print(folds)
    convert_dots(folds[0], dots)



if __name__ == "__main__":
    main()