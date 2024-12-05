# Day 4: Advent of Code 2024
# https://adventofcode.com/2024/day/4

# Input format:
# Lines of text representing a word search

# Goal: Find # of occurences of XMAS in word search style
# i.e. Forwards, backwards, vertical, and diagonal operations

class SearchCell:
    def __init__(self, row, col):
        self.upperBound = 0
        self.lowerBound = len(board) - 1
        self.leftBound = 0
        self.rightBound = len(board) - 1
        self.row = row
        self.col = col
        self.searchDirections = []
        # up, down, left, right, diagonal_up_left, diagonal_down_left, diagonal_up_right, diagonal_down_right
        for direction in availableDirections:
            maxPosition = [row + (direction[0] * (len(searchString) - 1)), col + (direction[1] * (len(searchString) -1))]
            if self.upperBound <= maxPosition[0] <= self.lowerBound and self.leftBound <= maxPosition[1] <= self.rightBound:
                self.searchDirections.append(direction)

    def checkDirection(self, row, col, direction, letterIndex = 1):
        if (letterIndex == 4):
            return True
        return self.checkDirection(row + direction[0], col + direction[1], direction, letterIndex + 1) if board[row][col] == searchString[letterIndex] else False
    
    def startSearch(self):
        sum = 0
        for direction in self.searchDirections:
            sum += self.checkDirection(self.row + direction[0], self.col + direction[1], direction)
        return sum

# Read input & append to lists
file = open("input.txt", "r")

board = []

for line in file:
    # Append line without newline character to board
    board.append(list(line.rstrip()))

file.close()

searchString = ['X', 'M', 'A', 'S']
availableDirections = [[1,0], [-1,0], [0,-1], [0,1], [1,-1], [-1,-1], [1,1], [-1,1]]
sum = 0

for row in range(0, len(board)):
    for col in range(0, len(board[row])):
        if (board[row][col] == searchString[0]):
            sum += SearchCell(row, col).startSearch()

print(sum)