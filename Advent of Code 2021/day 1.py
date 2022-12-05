import os

os.chdir("C:\\Users\\mathi\\OneDrive - NTNU\\Personlig\\Div kode\\Advent of Code 2021")

tst_input = [199
,200
,208
,210
,200
,207
,240
,269
,260
,263]

count = 0

with open("day_1_input.txt", 'r') as f:
    temp = f.readlines()
    input = []
    for string in temp:
        input.append(int(string.strip()))

def count_increasing(liste):
    count = 0
    for i, el in enumerate(liste):
        if i == 0:
            continue
        if el > liste[i-1]:
            count += 1

    return count


# Part 1
# for i, el in enumerate(input):
#     if i == 0:
#         continue
#     if el > input[i-1]:
#         count += 1

print(count_increasing(input))

# Part 2

count = 0
sliding_window = []

for i in range(0, len(input)):
    try:
        sliding_window.append(input[i] + input[i+1] + input[i+2])
    except:
        pass


# for i, el in enumerate(sliding_window):
#     if i == 0:
#         continue
#     if el > sliding_window[i-1]:
#         count += 1

print(count_increasing(sliding_window))