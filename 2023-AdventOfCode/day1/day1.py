import re


def read_file(file_path):
    with open(file_path, "r") as f:
        input_lines = f.read().splitlines()
    return input_lines


input_lines = read_file("input.txt")
example1 = read_file("example1.txt")
example2 = read_file("example2.txt")


# ############################################################################
# PART 1
def sum_all_digits(lines):
    total = []
    for line in lines:
        digit0 = re.search(r'(\d).*', line).groups()[0]
        digit1 = re.search(r'.*(\d)', line).groups()[0]
        digits = f'{digit0}{digit1}'
        total.append(int(digits))
    return total


total = sum_all_digits(input_lines)
print(total)
# total = 56108



# ############################################################################
# PART 2
numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
numbers_dict = {
    "one": "1", "two": "2", "three": "3", "four": "4", "five": "5",
    "six": "6", "seven": "7", "eight": "8", "nine": "9"
}

def get_digit(digit):
    if (digit.isdigit()):
        return digit
    else:
        return numbers_dict[digit]


new_lines = []
for line in input_lines:
    # IMPORTANT! Lookahed not to "consume" the match
    matches = re.findall(r'(?=(one|two|three|four|five|six|seven|eight|nine|\d))', line)
    num_l, num_r = get_digit(matches[0]), get_digit(matches[-1])
    new_lines += [f"{num_l}{num_r}"]

new_digits = sum_all_digits(new_lines)
sum(new_digits)
# total = 55652
