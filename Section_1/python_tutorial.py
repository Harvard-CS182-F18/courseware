#######################
## CS 182: SECTION 1 ##
##  Python Tutorial  ##
#######################

## ------------------ Variables and Printing ------------------

## initialize variables of different types
a = 2
b = "pangolin"
c = 0.00018

## print this variables
print a

## can also print like this
print "b is", b
print "c is {}".format(c)

## this does not work because 'a' is not a string!
# print "a is" + a

## instead, try this:
print "a is " + str(a)

## mathematical operations:
print "a + 5 =", a + 5
print "a * (-4.5) =", a * (-4.5)

# 'c += 1' is shorthand for c = c + 1
# 'c -= 1' is shorthand for c = c - 1
c += 1
print "c is now", c
c -= 1
print "c is now", c

## be careful of dynamic typing with division!
print "a/3 =", a/3
print "a/3. =", a/3.

## booleans: how do we represent true or false values?
print "'a == 2' returns ", a == 2
print "'a != 2' returns ", a != 2
print "'a < 10' returns ", a < 10
print "'a > 10' returns ", a > 10

## What do you think will happen if these comparisons are done with the variable 'b'? Why? Try it and see if you guessed correctly!


## ------------------ Data structures: Lists, Sets, and Dictionaries ------------------

## a list can hold items
courses1 = ['CS50', 'CS182', 'AM205']
print courses1

## the items don't have to have the same type
courses2 = ['CS50', 'CS182', 'AM205', 100]
print courses2

## use 0-based indexing to get specific items
print "courses1[0] returns", courses1[0]
print "courses2[3] returns", courses2[3]

## to get multiple items, slice the list with a colon (note that the end index is NOT included)
print "courses2[1:3] returns", courses2[1:3]

## to get elements from the end, reverse the indexing
print "courses2[-1] returns", courses2[-1]

## we can not assign items to list indices that don't exist yet
#courses1[3] = "PSY1401"

## instead, append to the end of a list
courses1.append("PSY1401")
print "after the append, courses1 is", courses1

## we can have duplicate elements
courses1.append("PSY1401")
print "after the append, courses1 is", courses1

## use 'pop' to remove and return the last element
print "courses1.pop() is", courses1.pop()

## Python also has sets! Sets do not hold duplicates, and unlike lists, they do not have an ordering.
print "set(courses1) is", set(courses1)

## Python also has dictionaries (also known as hashtables)! Dictionaries map specific "keys" to their "values". For instance, in the following dictionary, the class numbers are keys, and the class descriptions are values.
courseDescriptions = {"CS50": "Introduction to Computer Science I", "CS153": "Compilers", "CS181": "Machine Learning", "CS182": "Artificial Intelligence"}

# get specific class descriptions
print "courseDescriptions['CS50'] =", courseDescriptions['CS50']
print "courseDescriptions['CS182'] =", courseDescriptions['CS182']

# get the list of keys and the list of values
print "courseDescriptions.keys() =", courseDescriptions.keys()
print "courseDescriptions.values() =", courseDescriptions.values()


## ------------------ Loops and Conditionals ------------------

# conditionals (if-statements)
if 1 + 1 == 11:
    print "Something's wrong :("
elif 1 + 1 == 2:
    print "Correct! :D"
else:
    print "Also wrong :("

# range(n) is a useful function that returns a list counting from 0 to n-1.
print(range(5))

# for loops
for i in range(5):
    print "i =", i, "; i**2 =", i**2

# while loops
i = 6
while i > 0:
    print i, "..."
    i = i - 1
    if i == 0:
        print "ZERO!"

# we can also use loops to iterate through data structures:
for key, value in courseDescriptions.iteritems():
    print "{}: {}".format(key, value)

## ------------------ Functions ------------------

## this is a simple function
def printCube(n):
    print n, "cubed is", n**3

## this is how to call the function
printCube(6)
printCube(-8)

## functions can also return values
def squareAndCube(n):
    n_squared = n**2
    n_cubed = n**3
    print n, "squared is", n_squared, "and cubed is", n_cubed
    return n_squared, n_cubed

## call the function and save/print returned values
x, y = squareAndCube(9)
print "x =", x, "and y =", y

## note the scope of variables in a Python script: since we defined courseDescriptions in the script above, it has global scope, and is accessible in the body of the function.
def printCourseDescription(courseName):
    print courseDescriptions[courseName]

## test this function
printCourseDescription("CS50")

## but what if the course does not exist in our dictionary?
# printCourseDescription("CS121")

## let's change the function -- dictionaries have a 'get' function that does not throw errors
def printCourseDescription(courseName):
    print courseDescriptions.get(courseName, "Course not found")

## test this function
printCourseDescription("CS50")
printCourseDescription("CS121")

# alternatively, we can catch the error
def printCourseDescription(courseName):
    try:
        print courseDescriptions[courseName]
    except:
        print "Course not found"

## test this function
printCourseDescription("CS50")
printCourseDescription("CS121")

# Python also has lambda functions (also called lambdas, lambda operators, or anonymous functions). This is a shortcut for creating small functions consisting of a single expression. For instance, this lambda adds 'x' and 'y':
multiplyLambda = lambda x, y: x * y
print multiplyLambda(2, 3)

# Lambda functions are especially useful in cases where simple functions are passed as arguments to more complex functions. However, there are limitations on what a lambda can contain -- for instance, before Python 3, a lambda could not contain a "print" statement, as that was already a full expression.


## ------------------ Classes and Objects ------------------

## We have used several functions of objects so far:
##    .format() for Strings
##    .append() and .pop() for Lists
##    .keys(), .values(), and .iteritems() for Dictionaries
## Why does this work? All of those are objects with pre-defined functions. If you have not heard about object-oriented programming before, objects are instances of classes. A class is a blueprint that you can define.
## An example class could be 'Car' with variables 'max_speed', or 'price', and functions 'return_diesel_measurement()' and 'shift_gear_up()'. We can create specific individual objects such as 'BMW' or 'VW' in which these variables are set to different values.
## The same principle applies to lists, dictionaries, strings and so on. Every time you create one of those, you instantiate the pre-defined class and have access to the functions.

## Let's create a very simple car class! By convention, class names are capitalized.
class Car:
    pass

## The variable 'prius' is an instance of the 'Car' class.
prius = Car()
print prius

## Now let's add some methods. First, the constructor: a function called '__init__' that is automatically called when a Car object is initialized. It sets values to the Car's fields: the 'name' and the 'position'. The keyword 'self' is similar to javascript 'this' and references the current object. The first argument of every method has to be this reference, and is implicit.
class Car:
    def __init__(self, name):
        self.name = name
        self.position = [0,0]

## The String argument below corresponds to the second argument to the __init__ method above.
prius = Car("Toyota Prius")
print prius

## How can we make 'print' more meaningful? Add a '__str__' function that returns a String.
class Car:
    def __init__(self, name):
        self.name = name
        self.position = [0,0]
    
    def __str__(self):
        return "A car named {}!".format(self.name)

## The String argument below corresponds to the second argument to the __init__ method above.
prius = Car("Toyota Prius")
outback = Car("Subaru Outback")
print prius
print outback


## ------------------ Packages ------------------

## Python has a whole world of packages that you can use. In particular, 'numpy', 'scipy', and 'sklearn' are useful packages for projects involving linear algebra, statistics, machine learning, etc. There are also packages for visualization: 'pyplot' from 'matplotlib' can make nice plots, and is even better when coupled with 'seaborn'.

## To initialize a module and be able to access its functions in a package, use 'import'. By convention, all import statements should be at the very start of the Python file.
import numpy
print numpy.array([[1, 2, 3], [4, 5, 6]])

## Since module names can be long, it is common to use the 'as' command to alias the package name by a shorter word. For the 'numpy' package, it is common to use 'np'.
import numpy as np
print np.array([[1, 2, 3], [4, 5, 6]])

## For plotting:
import matplotlib.pyplot as plt

plt.figure()
plt.plot([0, 1, 2, 3, 4, 5], [0, 1, 4, 9, 16, 25], 'b*-')
plt.title("It's a plot!")
plt.show() # don't forget this line -- it actually creates the figure on the screen!
