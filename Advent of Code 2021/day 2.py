# import os
import ReadFile

# os.chdir("C:\\Users\\mathi\\OneDrive - NTNU\\Personlig\\Div kode\\Advent of Code 2021")

forward = 0
depth = 0

# commands = []
# # -- part 1 --
# with open("day_2_input.txt", 'r') as f:
#     for el in f.readlines():
#         commands.append(el.rstrip().split(" "))

commands = ReadFile.getList("day_2_input.txt")

for cmd, no in commands:
    if cmd == "forward":
        forward += int(no)
    elif cmd == "down":
        depth += int(no)
    else:
        depth -= int(no)

print("Part 1:")
print(forward * depth)

forward = 0
depth = 0
aim = 0

for cmd in commands:
    if cmd[0] == "forward":
        forward += int(cmd[1])
        depth += (int(cmd[1]) * int(aim))

    elif cmd[0] == "down":
        aim += int(cmd[1])

    else:
        aim -= int(cmd[1])

print("Part 2:")
print(forward * depth)

