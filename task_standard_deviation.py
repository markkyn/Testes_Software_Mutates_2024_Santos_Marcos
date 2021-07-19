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
