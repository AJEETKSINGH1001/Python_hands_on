'''
A Python function is a block of organized, reusable code that is used to perform a single, related action. Functions provide better modularity for your application and a high degree of code reusing.
A top-to-down approach towards building the processing logic involves defining blocks of independent reusable functions. A Python function may be invoked from any other function by passing required data (called parameters or arguments).
The called function returns its result back to the calling environment.

Function blocks begin with the keyword def followed by the function name and parentheses ( ( ) ).
Any input parameters or arguments should be placed within these parentheses. You can also define parameters inside these parentheses.
The first statement of a function can be an optional statement; the documentation string of the function or docstring.
The code block within every function starts with a colon (:) and is indented.
The statement return [expression] exits a function, optionally passing back an expression to the caller.
A return statement with no arguments is the same as return None.
'''

def greetings():
   "This is docstring of greetings function"
   print ("Hello World")
   return
greetings()

#Calling a Function in Python

# Function definition is here
def printme( str ):
   "This prints a passed string into this function"
   print (str)
   return;

# Now you can call printme function
printme("I'm first call to user defined function!")
printme("Again second call to the same function")

'''
The function calling mechanism of Python differs from that of C and C++. There are two main function calling mechanisms: Call by Value and Call by Reference.
When a variable is passed to a function, what does the function do to it? If any changes to its
variable doesnot get reflected in the actual argument, then it uses call by value mechanism. 
'''
def testfunction(arg):
   print ("ID inside the function:", id(arg))

var="Hello"
print ("ID before passing:", id(var))
testfunction(var)

'''
Python numeric object is immutable. When a numeric object is passed, 
and then the function changes the value of the formal argument, it actually creates a new object in the memory, 
leaving the original variable unchanged.
'''
def testfunction(arg):
   print ("ID inside the function:", id(arg))
   arg=arg+1
   print ("new object after increment", arg, id(arg))

var=10
print ("ID before passing:", id(var))
testfunction(var)
print ("value after function call", var)

#Pass by reference function
def testfunction(arg):
    print("Inside function:", arg)
    print("ID inside the function:", id(arg))
    arg = arg.append(100)


var = [10, 20, 30, 40]
print("ID before passing:", id(var))
testfunction(var)
print("list after function call", var)
