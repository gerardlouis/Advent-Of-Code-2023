# --- Part Two ---
# Your calculation isn't quite right. It looks like some of the digits are actually spelled out with letters: one, two, three, four, five, six, seven, eight, and nine also count as valid "digits".

# Equipped with this new information, you now need to find the real first and last digit on each line. For example:

# two1nine
# eightwothree
# abcone2threexyz
# xtwone3four
# 4nineeightseven2
# zoneight234
# 7pqrstsixteen
# In this example, the calibration values are 29, 83, 13, 24, 42, 14, and 76. Adding these together produces 281.

# What is the sum of all of the calibration values?

import re

number_string_dict = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
}

number_string_regex = '\\d|' + '|'.join(list(number_string_dict.keys()))
number_string_reverse_regex = '\\d|' + '|'.join(i[::-1] for i in list(number_string_dict.keys()))

# input = open('day01-example-input.txt', 'r')
input = open('day01-input.txt', 'r')
lines = input.readlines()
sum = 0

for line in lines:
    first_digit = re.search(number_string_regex, line).group()
    last_digit = re.search(number_string_reverse_regex, line[::-1]).group()
    if not first_digit.isnumeric():
        if first_digit in number_string_dict.keys():
            first_digit = number_string_dict[first_digit]
    if not last_digit.isnumeric():
        if last_digit[::-1] in number_string_dict.keys():
            last_digit = number_string_dict[last_digit[::-1]]
    calibration_value = int(first_digit + last_digit)
    # print('Calibration Value: ' + str(calibration_value))
    sum = sum + calibration_value

print('Sum of Calibration Values: ' + str(sum))