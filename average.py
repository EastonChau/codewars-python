#Write a function which calculates the average of the numbers in a given array.

#Note: Empty arrays should return 0.

import statistics as sttt

def find_average(numbers):
    return 0 if len(numbers) == 0 else sttt.mean(numbers)
