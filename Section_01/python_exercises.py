#######################
## CS 182: SECTION 1 ##
##  Python Exercises ##
#######################

## ------------------ Exercise 1: Loops ------------------

# Write a program that sings the song "99 Bottles of Beer". The lyrics are as follows:

# ----------------
# 99 bottles of beer on the wall, 99 bottles of beer.
# Take one down and pass it around, 98 bottles of beer on the wall.

# 98 bottles of beer on the wall, 98 bottles of beer.
# Take one down and pass it around, 97 bottles of beer on the wall.

# ...

# 1 bottle of beer on the wall, 1 bottle of beer.
# Take one down and pass it around, no more bottles of beer on the wall.
# ----------------

# Make sure that you use the correct plural and singular form for "bottle".


## ------------------ Exercise 2: Classes and Objects ------------------

# This series of exercises will build off of the 'Classes and Object' review section in the tutorial.

# (1) Add a function moveRight() to the Car class that changes self.position so that the x-coordinate is incremented by 1 with each call.

# Next, we create a grid for the car to drive on.

class Grid:
    # We can give function parameters default values
    def __init__(self, size=10):
        # We support only square grids for now
        self.size = [size,size]

# (2) Add a function plotGrid() to the Grid class that prints every position as |_|. For instance, a 3x3 grid should look like this:

# |_| |_| |_|
# |_| |_| |_|
# |_| |_| |_|

# Now we can add objects to the grid. We can create a list that hold objects from our Car class, so that the constructor becomes:
class Grid:
    # We can give function parameters default values
    def __init__(self, size=10):
        # We support only square grids for now
        self.size = [size,size]
        self.objects = []

    def add_object(self, o):
        self.objects.append(o)

# (3) Extend the plotGrid() function so that every field which is occupied by a Car (based on the Car's 'position' fields) is printed as '|0|'.
