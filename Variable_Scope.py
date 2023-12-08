'''
A variable in Python is a symbols name to the object in computer's memory.
Python works on the concept of namespaces to define the context for various identifiers such as functions,
variables etc.
A namespace is a collection of symbolic names defined in the current context.
Built-in namespace contains built-in functions and built-in exceptions. They are loaded in the memory as soon as Python interpreter is loaded and remain till the interpreter is running.

Global namespace contains any names defined in the main program. These names remain in memory till the program is running.

Local namespace contains names defined inside a function. They are available till the function is running.

{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x00000263E7255250>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': 'C:\\Users\\user\\examples\\main.py', '__cached__': None, 'name': 'TutorialsPoint', 'marks': 50, 'result': True, 'myfunction':
<function myfunction at 0x00000263E72004A0>}
'''

name = 'TutorialsPoint'
marks = 50
result = True


def myfunction():
    a = 10
    b = 20
    return a + b


#print(globals()

#Globals

x = 5
y = 10
def sum():
   sum = x + y
   return sum
print(sum())

'''
Python locals() Function
Python's standard library includes a built-in function locals().
It returns a dictionary of symbols currently available in the local namespace of the function.
'''
name = 'TutorialsPoint'
marks = 50
result = True
def myfunction():
   a = 10
   b = 20
   c = a+b
   print ("globals():", globals())
   print ("locals():", locals())
   return c
myfunction()

def sum(x,y):
   sum = x + y
   return sum
print(sum(5, 10))

'''
Namespace Conflict in Python
If a variable of same name is present in global as well as local scope, 
Python interpreter gives priority to the one in local namespace.
'''
marks = 50  # this is a global variable

def myfunction():
    marks = 70  # this is a local variable
    print(marks)


myfunction()
print(marks)  # prints global value

#If you try to manipulate value of a global variable from inside a function,
# Python raises UnboundLocalError.

marks = 50 # this is a global variable
def myfunction():
  # marks = marks + 20
   print (marks)

myfunction()
print (marks) # prints global value

#To modify a global variable, you can either update it with a dictionary syntax,
# or use the global keyword to refer it before modifying.

var1 = 50 # this is a global variable
var2 = 60 # this is a global variable
def myfunction():
   "Change values of global variables"
   globals()['var1'] = globals()['var1']+10
   global var2
   var2 = var2 + 20

myfunction()
print ("var1:",var1, "var2:",var2) #shows global variables with changed values

#if you try to access a local variable in global scope,
#Python raises NameError as the variable in local scope can't be accessed outside it.

var1 = 50 # this is a global variable
var2 = 60 # this is a global variable
def myfunction(x, y):
    
   total = x+y
   print ("Total is a local variable: ", total)

myfunction(var1, var2)
print (total) # This gives NameError





