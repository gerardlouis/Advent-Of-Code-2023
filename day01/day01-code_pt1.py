# As they're making the final adjustments, they discover that their calibration document (your puzzle input) has been amended by a very young Elf who was apparently just excited to show off her art skills. Consequently, the Elves are having trouble reading the values on the document.

# The newly-improved calibration document consists of lines of text; each line originally contained a specific calibration value that the Elves now need to recover. On each line, the calibration value can be found by combining the first digit and the last digit (in that order) to form a single two-digit number.

# For example:

# 1abc2
# pqr3stu8vwx
# a1b2c3d4e5f
# treb7uchet
# In this example, the calibration values of these four lines are 12, 38, 15, and 77. Adding these together produces 142.

# Consider your entire calibration document. What is the sum of all of the calibration values?

import re

# input = open('day01-example-input.txt', 'r')
input = open('day01-input.txt', 'r')
lines = input.readlines()
sum = 0

for line in lines:
    first_digit = re.search(r'\d', line).group()
    last_digit = re.search(r'\d', line[::-1]).group()
    calibration_value = int(first_digit + last_digit)
    sum = sum + calibration_value

print('Sum of Calibration Values: ' + str(sum))