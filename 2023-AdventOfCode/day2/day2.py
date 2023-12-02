import re


def read_file(file_path):
    with open(file_path, "r") as f:
        input_lines = f.read().splitlines()
    return input_lines


input_lines = read_file("input.txt")
example1 = read_file("example1.txt")
example2 = read_file("example2.txt")


class Reveal:
    def __init__(self, red, green, blue):
        self.R = red
        self.G = green
        self.B = blue
    def __repr__(self):
        return f"R:{self.R} G:{self.G} B:{self.B}"


class Game:
    def __init__(self):
        self.id = 0
        self.reveals = []
    def __str__(self):
        return f"Game {self.id}: {self.reveals}"
    def __repr__(self):
        return f"Game {self.id}: {self.reveals}"

class GameParser:
    def __init__(self, lines: str):
        self.games = []
        self._parse_input(lines)
    def _parse_input(self, lines):
        for line in lines:
            game = Game()
            gameid_text, reveals_text = line.split(": ")
            game.id = int(re.findall("Game (\d+)", gameid_text)[0])
            reveals_lines = reveals_text.split("; ")
            for reveal_line in reveals_lines:
                r = re.findall('(\d+) red', reveal_line) or ['0']
                g = re.findall('(\d+) green', reveal_line) or ['0']
                b = re.findall('(\d+) blue', reveal_line) or ['0']
                r, g, b = int(r[0]), int(g[0]), int(b[0])
                game.reveals.append(Reveal(r, g, b))
            self.games.append(game)


gp = GameParser(input_lines)
gp = GameParser(example1)


# ############################################################################
# PART 1
MAX_R, MAX_G, MAX_B = 12, 13, 14
rr = [game.id for game in gp.games if all([reveal.R <= MAX_R for reveal in game.reveals])]
gg = [game.id for game in gp.games if all([reveal.G <= MAX_G for reveal in game.reveals])]
bb = [game.id for game in gp.games if all([reveal.B <= MAX_B for reveal in game.reveals])]

# intersection games that are possible for all colors
possible_games = list( set(rr).intersection(gg, bb) )
print(sum(possible_games))
# 3099



# ############################################################################
# PART 2
max_values = [(  max(r.R for r in game.reveals), max(r.G for r in game.reveals),
    max(r.B for r in game.reveals)) for game in gp.games]

powers = [m[0]*m[1]*m[2] for m in max_values]
sum(powers)
# 72970 