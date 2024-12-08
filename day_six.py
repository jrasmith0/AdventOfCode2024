# Day 6: Advent of Code 2024
# https://adventofcode.com/2024/day/6

# Input format:
# Lines of text representing a floor layout featuring obstacles and a guard

# Find the path the guard takes, returning the distinct positions the guard travels on

# Read input & append to lists
file = open("input.txt", "r")
map = []

orientations = {'^', '>', '<', 'V'}

class Guard:
    location = [-1, -1]
    directionDict = {'^':[-1,0], '>':[0,1], '<':[0,-1], 'V':[1,0]}

    def __init__(self, location, orientation):
        self.positionsVisited = 1
        self.location = location
        self.orientation = orientation

    def inBoundsPosition(self, position):
        return True if (0 <= position[0] <= len(map) - 1 and 0 <= position[1] <= len(map[0]) - 1) else False

    def inBounds(self):
        position = [self.location[0], self.location[1]]
        return self.inBoundsPosition(position)

    def turnRight(self):
        if (self.orientation == '^'):
            self.orientation = '>'
        elif (self.orientation == '>'):
            self.orientation = 'V'
        elif (self.orientation == 'V'):
            self.orientation = '<'
        else:
            self.orientation = '^'

    def move(self):
        add = lambda a, b : [a[0] + b[0], a[1] + b[1]]
        potentialMove = add(self.location, self.directionDict[self.orientation])
        if (not self.inBoundsPosition(potentialMove)):
            self.location = potentialMove
        else:
            if (map[potentialMove[0]][potentialMove[1]] == '#'):
                # Path is blocked, so turn right and advance
                self.turnRight()
                self.move()
            else:
                self.location = potentialMove
                if (map[self.location[0]][self.location[1]] != 'X'):
                    map[self.location[0]][self.location[1]] = 'X'
                    self.positionsVisited += 1



guardValues = []
row = 0
for line in file:
    # Append line without newline character to board
    for i in range(0, len(line)):
        # Find index of guard
        if (line[i] in orientations):
            # Location, Orientation
            guardValues = [[row, i], line[i]]

    map.append(list(line.rstrip()))
    row += 1

file.close()

guard = Guard(guardValues[0], guardValues[1])

# Replace value of guard with X on map
map[guard.location[0]][guard.location[1]] = 'X'

while(guard.inBounds()):
    guard.move()

print(guard.positionsVisited)
