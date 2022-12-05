import os

os.chdir("C:\\Users\\mathi\\OneDrive - NTNU\\Personlig\\Div kode\\Advent of Code 2021")


class bingoNumber:

    def __init__(self, num) -> None:
        self.num = num
        self.marked = False

    def __repr__(self) -> str:
        return f"({self.num}, {self.marked})"

    def mark(self) -> None:
        self.marked = True

class bingoCard:

    def __init__(self, numbers: list) -> None:
        self.card = []
        for el in numbers:
            ind_nums = (el.split())
            row = []
            for num in ind_nums:
                row.append(bingoNumber(int(num)))

            self.card.append(row)
        # print(self.card)
        # print("\n")

    def __repr__(self) -> str:
        rep = f"{self.card[0]}\n{self.card[1]}\n{self.card[2]}\n{self.card[3]}\n{self.card[4]}\n"
        return rep

    def mark_number(self, row: int, col: int) -> None:
        self.card[row][col].mark()

def check_win(bingoCard: bingoCard) -> bool:
    for i in range(5):
        if bingoCard.card[i][0].marked & bingoCard.card[i][1].marked & bingoCard.card[i][2].marked & bingoCard.card[i][3].marked & bingoCard.card[i][4].marked:
            return True
        if bingoCard.card[0][i].marked & bingoCard.card[1][i].marked & bingoCard.card[2][i].marked & bingoCard.card[3][i].marked & bingoCard.card[4][i].marked:
            return True

bingo_nums = None

bingo_cards = []

with open("day_4_input.txt", 'r', encoding = 'UTF-8') as f:
    raw_data = f.readlines()
    bingo_nums = raw_data[0]
    for i in range(1, len(raw_data), 6):
        tmp_list = []
        for j in range(6):

            tmp_list.append(raw_data[i+j].rstrip("\n"))
        
        bingo_cards.append(tmp_list[1:])
    
# print(raw_data)
# print(bingo_nums)
# print(bingo_cards)

# print(bingo_cards[1])

list_of_bingos = []
for el in bingo_cards:
    tmp = bingoCard(el)
    list_of_bingos.append(tmp)
    tmp = None

# print(list_of_bingos)

bingo_nums = bingo_nums.split(",")

def checking():
    bingo: bingoCard
    check_win_count = 0
    won_bingos = []
    for num in bingo_nums:
        for bingo in list_of_bingos:
            if bingo in won_bingos:
                continue
            for i in range(5):
                for j in range(5):
                    if int(bingo.card[i][j].num) == int(num):
                        bingo.mark_number(i, j)
            # print(bingo)
            if check_win(bingo):
                won_bingos.append(bingo)
                check_win_count += 1
                # print(check_win_count)
                if check_win_count == len(list_of_bingos):

                    print(num)

                    print(bingo)
                # print(list_of_bingos)
                    return

checking()
# print(list_of_bingos)