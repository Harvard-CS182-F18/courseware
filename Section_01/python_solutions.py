#######################
## CS 182: SECTION 1 ##
##  Python Solutions ##
#######################

## ------------------ Exercise 1: Loops ------------------

for i in range(99, 0, -1):
    if i > 1:
        print "{} bottles of beer on the wall, {} bottles of beer.".format(i, i)
        if i > 2:
            end = "{} bottles of beer on the wall.".format(i-1)
        else:
            end = "1 bottle of beer on the wall."
    else:
        print "1 bottle of beer on the wall, 1 bottle of beer."
        end = "no more bottles of beer on the wall!"
    print "Take one down, pass it around,", end
    print

## ------------------ Exercise 2: Classes and Objects ------------------

class Grid:
    def __init__(self, size=10):
        self.size = [size,size]
        self.objects = []
    
    def plotGrid(self):
        for y in xrange(self.size[1]):
            for x in xrange(self.size[0]):
                has_object = False
                for o in self.objects:
                    if o.position == [x,y]:
                        has_object = True
                if has_object:
                    print "|O|",
                else:
                    print "|_|",
            print ""
    
    def addObject(self, o):
        self.objects.append(o)

# car class for testing the grid (the 'moveDown' method was added for better testing.)
class Car:
    def __init__(self, name):
        self.name = name
        self.position = [0,0]
    
    def __str__(self):
        return "A car named {}!".format(self.name)
    
    def moveRight(self):
        self.position[0] += 1

    def moveDown(self):
        self.position[1] += 1

# make a prius!
prius = Car("Prius")
print prius

# plot the grid with no objects
grid = Grid(6)
grid.plotGrid()
print

# plot the grid with an object at (0, 0)
grid.addObject(prius)
grid.plotGrid()
print

# plot the grid with an object at (3, 2)
prius.moveRight()
prius.moveDown()
prius.moveDown()
prius.moveDown()
prius.moveRight()
grid.plotGrid()


