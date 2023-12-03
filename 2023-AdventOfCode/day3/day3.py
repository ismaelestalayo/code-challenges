from functools import reduce

import re


def read_file(file_path):
    with open(file_path, "r") as f:
        input_lines = f.read().splitlines()
    return input_lines


inp_lines = read_file("input.txt")
ex1_lines = read_file("example1.txt")


# ############################################################################
# PART 1
INPUT_LINES = inp_lines
MATCHES = []
prev_line = "." * len(INPUT_LINES[0])
for i, curr_line in enumerate(INPUT_LINES):
    next_line = INPUT_LINES[i + 1] if i < len(INPUT_LINES) - 1 else "." * len(INPUT_LINES[0])
    # print("\n", "-" * 150)
    # print("PREV: ", prev_line)
    # print("CURR: ", curr_line)
    # print("NEXT: ", next_line)
    # find numbers
    matches = re.findall('(\d+)', curr_line)
    print(curr_line)
    for match in matches:
        print(match)
        index = re.search(rf'\b{match}\b', curr_line).span()[0]
        start_index = index - 1 if index > 0 else 0
        m_p = re.search('[^0-9.\n]', prev_line[start_index : index + len(match) + 1] )
        m_c = re.search('[^0-9.\n]', curr_line[start_index : index + len(match) + 1] )
        m_n = re.search('[^0-9.\n]', next_line[start_index : index + len(match) + 1] )
        if (m_p or m_c or m_n):
            # print("!!!!!!!!: ", match)
            MATCHES.append(int(match))
    # 
    prev_line = curr_line


print(sum(MATCHES)) # 532331



# ############################################################################
# PART 2
INPUT_LINES = ex1_lines
INPUT_LINES = inp_lines

TOTAL_SUM = 0
prev_line = "." * len(INPUT_LINES[0])
for i, curr_line in enumerate(INPUT_LINES):
    next_line = INPUT_LINES[i + 1] if i < len(INPUT_LINES) - 1 else "." * len(INPUT_LINES[0])
    # print("\n", "-" * 120)
    # print("PREV: ", prev_line)
    # print("CURR: ", curr_line)
    # print("NEXT: ", next_line)
    # find "*"s
    star_indexes = [m.start() for m in re.finditer(r'\*', curr_line)]
    # 
    for star_index in star_indexes:
        m_p = [prev_line[match[0]:match[1]] for match in [(m.start(), m.end()) for m in re.finditer(r'(\d+)', prev_line)] if ((star_index - 1 <= match[0] <= star_index + 1) or (star_index <= match[1] <= star_index + 1 )) ]
        m_c = [curr_line[match[0]:match[1]] for match in [(m.start(), m.end()) for m in re.finditer(r'(\d+)', curr_line)] if ((star_index - 1 <= match[0] <= star_index + 1) or (star_index <= match[1] <= star_index + 1 )) ]
        m_n = [next_line[match[0]:match[1]] for match in [(m.start(), m.end()) for m in re.finditer(r'(\d+)', next_line)] if ((star_index - 1 <= match[0] <= star_index + 1) or (star_index <= match[1] <= star_index + 1 )) ]
        all_matches = m_p + m_c + m_n
        if (len(all_matches) == 2):
            # print("!!!!!!!!: ", all_matches)
            product = reduce(lambda x,y: x*y, map(int, all_matches))
            TOTAL_SUM += product
        # 
    prev_line = curr_line


print(TOTAL_SUM) # 82301120
