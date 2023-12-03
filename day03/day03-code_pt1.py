# --- Day 3: Gear Ratios ---
# You and the Elf eventually reach a gondola lift station; he says the gondola lift will take you up to the water source, but this is as far as he can bring you. You go inside.

# It doesn't take long to find the gondolas, but there seems to be a problem: they're not moving.

# "Aaah!"

# You turn around to see a slightly-greasy Elf with a wrench and a look of surprise. "Sorry, I wasn't expecting anyone! The gondola lift isn't working right now; it'll still be a while before I can fix it." You offer to help.
# The engineer explains that an engine part seems to be missing from the engine, but nobody can figure out which one. If you can add up all the part numbers in the engine schematic, it should be easy to work out which part is missing.

# The engine schematic (your puzzle input) consists of a visual representation of the engine. There are lots of numbers and symbols you don't really understand, but apparently any number adjacent to a symbol, even diagonally, is a "part number" and should be included in your sum. (Periods (.) do not count as a symbol.)

# Here is an example engine schematic:

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
# In this schematic, two numbers are not part numbers because they are not adjacent to a symbol: 114 (top right) and 58 (middle right). Every other number is adjacent to a symbol and so is a part number; their sum is 4361.

# Of course, the actual engine schematic is much larger. What is the sum of all of the part numbers in the engine schematic?

# input = open('day03/day03-example-input.txt', 'r')
input = open('day03/day03-input.txt', 'r')
lines = input.readlines()
last_character_is_number = False
start_column = 0
number = ''
symbols = []
numbers = {}
part_numbers = []

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
            if line[column] != '.' and line[column] != '\n':
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

    for i in range(row-1,row+2):
        for j in range(column-1,column+2):
            if i in numbers:
                if not (i == row and j == column) and j in numbers[i]:
                    if prev_part_number != numbers[i][j]:
                        part_numbers.append(numbers[i][j])
                        prev_part_number = numbers[i][j]

# print('Part Numbers: ' + str(list(part_numbers)))
print('Sum of Part Numbers: ' + str(sum(list(part_numbers))))