import os

os.chdir("C:\\Users\\mathi\\OneDrive - NTNU\\Personlig\\Div kode\\Advent of Code 2021")


liste = []

with open("day_3_input.txt", 'r') as f:
    liste = f.read().split('\n')


# -- part 1 --
max_range = len(liste)

summer = []

for i in range(len(liste[1])):
    sum = 0
    for j in range(max_range):
        # print(liste[i][0])
        sum += eval(liste[j][i])
        
    summer.append(sum)

# print(summer)
gamma = ""
epsilon = ""
for i in summer:
    if i > 500:
        gamma += '1'
        epsilon += '0'
    else:
        gamma += '0'
        epsilon += '1'

# print(f"Gamma: {gamma}")
# print(f"epsilon: {epsilon}")

gamma = (int(gamma, base = 2))
epsilon = (int(epsilon, base = 2))

# print(gamma * epsilon)

# def oxygen_rating(liste: list) -> list:
def get_most_common(liste: list, col: int, reversed: bool = False):
    current_sum = 0
    for i in range(len(liste)):
        # print(liste[i][col])
        current_sum += int(liste[i][col])

    # print(current_sum)
    # print(len(liste)/2)
    if current_sum >= (len(liste)/2):
        if reversed == False: return 1
        return 0
    if reversed == False: return 0
    return 1

# -- part 2 --
# print(summer)

# print(get_most_common(liste, 0, True))

def remove_elements(liste: list, col: int, reversed: bool = False):
    new_list = []

    most_common = get_most_common(liste, col, reversed)
    # print(most_common)
    for i, el in enumerate(liste):
        if int(el[col]) == int(most_common):
            new_list.append(el)

    return new_list


# t = remove_elements(liste, 0)
# print(len(t))
# t2 = remove_elements(t, 1)
# print(len(t2))

# liste = ["00100",
# "11110",
# "10110",
# "10111",
# "10101",
# "01111",
# "00111",
# "11100",
# "10000",
# "11001",
# "00010",
# "01010"]

t = liste
for i in range(12):
    t = remove_elements(t, i)
    if (len(t) == 1):
        break

print("Most common:" + str(t))
ox = int(t[0], base = 2)
print(ox)

t = liste

for i in range(12):
    t = remove_elements(t, i, True)
    if (len(t) == 1):
        break

print(t)
co2 = int(t[0], base = 2)
print(co2)

print(ox * co2)
