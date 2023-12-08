'''
The concept of module in Python further enhances the modularity.
You can define more than one related functions together and load required functions. A module is a file containing definition of functions, classes, variables, constants or any other Python object. Contents of this file can be made available to any other program.
Python has the import keyword for this purpose.

Module Attributes
In Python, a module is an object of module class, and hence it is characterized by attributes.

Following are the module attributes −

__file__ returns the physical name of the module.

__package__ returns the package to which the module belongs.

__doc__ returns the docstring at the top of the module if any

__dict__ returns the entire scope of the module

__name__ returns the name of the module
'''

import math
print ("Square root of 100:", math.sqrt(100))

"The docstring of mymodule"


def sum(x, y):
    return x + y


print("sum:", sum(10, 20))


"The docstring of mymodule"
def sum(x,y):
   return x+y

if __name__ == "__main__":
   print ("sum:",sum(10,20))


def SayHello(name, course):
   print ("Hi {}! How are you?".format(name))
   print ("Welcome to {} Tutorial by TutorialsPoint".format(course))
   return
