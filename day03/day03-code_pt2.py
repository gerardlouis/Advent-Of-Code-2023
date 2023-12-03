# --- Part Two ---
# The engineer finds the missing part and installs it in the engine! As the engine springs to life, you jump in the closest gondola, finally ready to ascend to the water source.

# You don't seem to be going very fast, though. Maybe something is still wrong? Fortunately, the gondola has a phone labeled "help", so you pick it up and the engineer answers.

# Before you can explain the situation, she suggests that you look out the window. There stands the engineer, holding a phone in one hand and waving with the other. You're going so slowly that you haven't even left the station. You exit the gondola.

# The missing part wasn't the only issue - one of the gears in the engine is wrong. A gear is any * symbol that is adjacent to exactly two part numbers. Its gear ratio is the result of multiplying those two numbers together.

# This time, you need to find the gear ratio of every gear and add them all up so that the engineer can figure out which gear needs to be replaced.

# Consider the same engine schematic again:

# 467..114..
# ...*......
# ..35..633.
# ......#...
# 617*......
# .....+.58.
# ..592.....
# ......755.
# ...$.*....
# .664.598..
# In this schematic, there are two gears. The first is in the top left; it has part numbers 467 and 35, so its gear ratio is 16345. The second gear is in the lower right; its gear ratio is 451490. (The * adjacent to 617 is not a gear because it is only adjacent to one part number.) Adding up all of the gear ratios produces 467835.

# What is the sum of all of the gear ratios in your engine schematic?

# input = open('day03/day03-example-input.txt', 'r')
input = open('day03/day03-input.txt', 'r')
lines = input.readlines()
last_character_is_number = False
start_column = 0
number = ''
symbols = []
numbers = {}
gear_ratios = []

# Add locations of all numbers and symbols
for row in range(0, len(lines)):
    line = lines[row]
    for column in range(0, len(line)):
        if line[column].isnumeric():
            if not last_character_is_number:
                start_column = column
            number = number + line[column]
            last_character_is_number = True
        else:
            if line[column] == '*':
                symbols.append((row, column))
            if last_character_is_number:
                last_character_is_number = False
                if row not in numbers:
                    numbers[row] = {}
                # print('Numbers: ' + str(numbers))    
                while start_column < column:
                    numbers[row][start_column] = int(number)
                    start_column = start_column + 1
                number = ''

# print('Symbols: ' + str(symbols))
# print('Numbers: ' + str(numbers))

prev_part_number = 0

# Check all locations for each symbol
for symbol in symbols:
    row = symbol[0]
    column = symbol[1]
    ratios = []

    for i in range(row-1,row+2):
        for j in range(column-1,column+2):
            if i in numbers:
                if not (i == row and j == column) and j in numbers[i]:
                    if prev_part_number != numbers[i][j]:
                        ratios.append(numbers[i][j])
                        prev_part_number = numbers[i][j]

    if len(ratios) == 2:
        gear_ratios.append(ratios[0] * ratios[1])

# print('Gear Ratios: ' + str(list(gear_ratios)))
print('Sum of Gear Ratio: ' + str(sum(list(gear_ratios))))