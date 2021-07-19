"""
This module contains the code for a task for the calculator.
The goal of this task is to demonstrate the functionality of
the calculator, more specifically the functionality of
standard_deviation module.
The task involves calculating the mean, population standard
deviation, and sample standard deviation of a set of values.
some values of the set are removed, added back, and lastly
the set is completely changed. The properties are calculated
at each step for comparison and analysis.
"""

from standard_deviation import StandardDeviation


std = StandardDeviation(10, 12, 23, 23, 16, 23, 21, 16)
print("Set of values:", std.get_values())
print("Mean:", std.get_mean())
print("Population Standard Deviation:", std.get_psd())
print("Sample Standard Deviation:", std.get_ssd())

# Remove the last two values
std.set_values(10, 12, 23, 23, 16, 23)
print("*******\n16 and 23 are removed from the set.")
print("Set of values:", std.get_values())
print("Mean:", std.get_mean())
print("Population Standard Deviation:", std.get_psd())
print("Sample Standard Deviation:", std.get_ssd())

# Add the values back to the set
std.add_values(21, 16)
print("*******\n16 and 23 are added back to the set.")
print("Set of values:", std.get_values())
print("Mean: ", std.get_mean())
print("Population Standard Deviation: ", std.get_psd())
print("Sample Standard Deviation: ", std.get_ssd())

# The set is completely changed
std.set_values(24, 57, 41, 38, 77, 63, 13, 80)
print("*******\nThe set is completely changed.")
print("Set of values:", std.get_values())
print("Mean:", std.get_mean())
print("Population Standard Deviation: ", std.get_psd())
print("Sample Standard Deviation: ", std.get_ssd())