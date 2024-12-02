# Day 1: Advent of Code 2024
# https://adventofcode.com/2024/day/1

# Imports
from collections import Counter

# Input format:
# Text file with numerical values separated by a space (i.e.)
# Each line corresponds to a pair to be compared
# 3 4
# 2 3

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


# Part 2
count = Counter(l2)

sum = 0
for num in l1:
    sum += count[num] * num

print (sum)