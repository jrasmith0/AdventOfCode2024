# Day 1: Advent of Code 2024
# https://adventofcode.com/2024/day/3

# Input format:
# Text document containing a wide range of characters that are pseudo "corrupted"

# Goal: 
# Look for strings in the sequence "mul(x,y)" where x, y are integers
# Multiply those integers, and sum up the result of all occurences of the search string

# Assumptions:
# File is not too large, so we're reading the entirety of the file at once

# Imports
import re

# Read from file
file = open("input.txt", "r")
txt = file.read()

# Close file read
file.close()

# Find all occurencers of "mul(x,y)" where x,y are integers of 1-3 digits in size
searchResult = re.findall("mul\\(\\d{1,3},\\d{1,3}\\)", txt)

def parseAndMultiply(x):
    vals = re.search("(\\d{1,3}),(\\d{1,3})", x).group().split(",")
    return int(vals[0]) * int(vals[1])

# Parse out the integers, convert them, multiply them and add them to running sum for each found instance
sum = 0
for x in searchResult:
    sum += parseAndMultiply(x)

print(sum)

# Part 2
adaptedSearchResult = re.findall("(mul\\(\\d{1,3},\\d{1,3}\\))|(do\\(\\))|(don't\\(\\))", txt)
adaptedSum = 0
enabled = True
for x in adaptedSearchResult:
    if(not x[0]):
        enabled = True if x[1] else False
    elif (enabled):
        adaptedSum += parseAndMultiply(x[0])

print(adaptedSum)