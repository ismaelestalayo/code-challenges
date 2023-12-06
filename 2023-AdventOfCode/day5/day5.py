import re


lines = open("input.txt").read()
lines = open("example1.txt").read()


# ############################################################################
# PART 1
lines = lines.split("\n\n")
lines = list(filter(None, lines))
print(f"\nLINES: \n{lines}")

# get seeds
seeds = map(int, re.findall('(\d+)', lines[0]))
seeds = list(seeds)
print(f"\nSEEDS: \n{seeds}")

# get conversios mappings
conversions = lines[1:]
print(f"\nCONVERSIONS: \n{conversions}")



# ############################################################################
# PART 2