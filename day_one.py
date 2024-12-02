# Day 1: Advent of Code 2024
# https://adventofcode.com/2024/day/1

l1 = []
l2 = []

# Read input & append to lists
file = open("input.txt", "r")
for line in file:
    tmp = line.split()
    l1.append(int(tmp[0]))
    l2.append(int(tmp[1]))

# Sort Lists to be able to compare min values against eachother
l1.sort()
l2.sort()

# Calculate abs diff between List1[x] to List2[x] & sum those values
print(sum([abs(ai - bi) for ai, bi in zip(l1, l2)]))