import os
from dataclasses import dataclass
import numpy as np
from collections import Counter

os.chdir("C:\\Users\\mathi\\OneDrive - NTNU\\Personlig\\Div kode\\Advent of Code 2021")

@dataclass
class Line:
    x1: int
    y1: int
    x2: int
    y2: int

    def start_point(self):
        return (self.x1,self.y1)

    def end_point(self):
        return (self.x2,self.y2)

    def get_all_points(self, diagonal: bool = False) -> list:
        points = []
        # if not diagonal:
        if self.x1 == self.x2 or self.y1 == self.y2:
            for i in range((self.x1 if self.x1 <= self.x2 else self.x2), (self.x2 if self.x2 >= self.x1 else self.x1)+1):
                for j in range((self.y1 if self.y1 <= self.y2 else self.y2), (self.y2 if self.y2 >= self.y1 else self.y1)+1):
                    tmp = [i ,j]
                    points.append(tuple(tmp))
        else:
            deltax = abs(self.x1 - self.x2)
            deltay = abs(self.y1 - self.y2)
            # print(deltax, deltay)
            startx = (self.x1 if self.x1 <= self.x2 else self.x2)
            starty = (self.y1 if self.y1 <= self.y2 else self.y2)
            tmp = []
            stepx = (1 if self.x1 < self.x2 else -1)
            stepy = (1 if self.y1 < self.y2 else -1)

            for i in range(self.x1, self.x2 + stepx, stepx):
                tmp.append([i])

            c = 0
            for j in range(self.y1, self.y2 + stepy, stepy):
                tmp[c].append(j)
                c += 1

            for i, el in enumerate(tmp):
                points.append(tuple(el))
        
        return(points)



lines = []

with open("day_5_input.txt", "r") as f:
    raw_data = f.readlines()

    for line in raw_data:
        two_parts = line.rstrip().split(" ->")
        x1 = int(two_parts[0].split(",")[0])
        y1 = int(two_parts[0].split(",")[1])
        x2 = int(two_parts[1].split(",")[0])
        y2 = int(two_parts[1].split(",")[1])
        lines.append(Line(x1,y1,x2,y2))


no_diagonal = []

for line in lines:
    if line.x1 == line.x2 or line.y1 == line.y2:
        no_diagonal.append(line)

# print(lines)
# print(no_diagonal)
# print(no_diagonal[0].get_all_points())

point_counter = []

for line in no_diagonal:
    for coord in line.get_all_points():
        point_counter.append(coord)

# print(point_counter)
counter = Counter(point_counter)

duplicate_counter = 0
for key in counter:

    if int(counter[key]) > 1:
        duplicate_counter += 1

print("Part 1: " + str(duplicate_counter))



# -- Part 2 --

point_counter = []
for line in lines:
    for coord in line.get_all_points():
        point_counter.append(coord)


# print(point_counter)

counter = Counter(point_counter)

# print(counter)
# print(lines[1])
# print(lines[1].get_all_points())

duplicate_counter = 0
for key in counter:

    if int(counter[key]) > 1:
        duplicate_counter += 1

print("Part 2: " + str(duplicate_counter))

# multiple = 0
# used_coord = []
# # print(point_counter)
# for coord in point_counter:
#     if coord not in used_coord:
#         used_coord.append(coord)
#     elif coord in used_coord:
#         multiple += 1

# print(multiple)









