# Day 2: Advent of Code 2024
# https://adventofcode.com/2024/day/2


# Part 1:
# Many reports... One per line of input, space separated

# Determine which reports are "Safe"
# Rules:
# 1) Values must be EITHER:
#     -> All Increasing
#     -> All Decreasing
# 2) Any two adjacent levels differ by at least 1 and at most 3

# Part 2:
# Apply a dampener where removing at most one value from the list can make the report pass

# Input format:
# Text file with numerical values separated by a space (i.e.)
# Each line corresponds to a new report
# 3 4 5 6 7

# Imports
import operator

# Define function to handle both rule cases:
def checkOrder(r):
    count = 0
    for i, j in zip(r, r[1:]):
        if j > i:
            count += 1
    return operator.gt if count > len(r) / 2 else operator.lt

def checkRules(s, i , j):
    return s(j, i) and (abs(i - j) >= 1 and abs(i - j) <= 3)

def inspectSafety(r):
    s = checkOrder(r)
    return all(checkRules(s, i, j) for i, j in zip(r, r[1:]))

def inspectSafetyWithDampener(r):
    s = checkOrder(r)
    index = 0
    for i, j in zip(r, r[1:]):
        if not(checkRules(s, i, j)):
            d = r.copy()
            del d[index]
            del r[index + 1]
            # Removing either i or j from the list applies the dampener
            return inspectSafety(d) or inspectSafety(r)
        index += 1
    return True

# Read from input file & process line by line
file = open("input.txt", "r") 

safeReports = 0
safeReportsWithDampener = 0
for line in file:
    report = [int(n) for n in line.split()]
    safeReports += inspectSafety(report)
    safeReportsWithDampener += inspectSafetyWithDampener(report)

print(safeReports)
print(safeReportsWithDampener)