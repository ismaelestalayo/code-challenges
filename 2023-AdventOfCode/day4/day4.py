import re


lines = open("example1.txt", "r").read().splitlines()

lines = open("input.txt", "r").read().splitlines()


# ############################################################################
# PART 1
WINS = 0
for line in lines:
    # remove the "Card X" beggining
    line = line.split(":")[1]
    # get all numbers
    nums_win, nums_all = [re.findall('(\d+)', numbers) for numbers in line.split("|")]
    # count winning numbers
    winning_numbers = len([n for n in nums_win if n in nums_all])
    points = 2 ** (winning_numbers-1)
    if (winning_numbers > 0):
        WINS += points

print("TOTAL:", WINS)



# ############################################################################
# PART 2
LINES_OBJ = list(zip([1]*len(lines), lines))
index = 0
for count, line in LINES_OBJ:
    # remove the "Card X" beggining
    line = line.split(":")[1]
    # get all numbers
    nums_win, nums_all = [re.findall('(\d+)', numbers) for numbers in line.split("|")]
    # count winning numbers
    winning_numbers = len([n for n in nums_win if n in nums_all])
    index += 1
    for c in range(count):
        for i in range(winning_numbers):
            LINES_OBJ[index+i] = (LINES_OBJ[index+i][0]+1, LINES_OBJ[index+i][1])
    # print(f"LINE {index}: {winning_numbers} winning numbers")
    # _ = [print(obj) for obj in LINES_OBJ]
    # print("-"*80)


sum([line_obj[0] for line_obj in LINES_OBJ])
# 9721255
