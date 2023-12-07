'''
The process of a function often depends on certain data provided to it while calling it.
While defining a function, you must give a list of variables in which the data passed to it is collected.
The variables in the parentheses are called formal arguments.
When the function is called, value to each of the formal arguments must be provided.
Those are called actual arguments.
'''


def greetings(name):
    "This is docstring of greetings function"
    print("Hello {}".format(name))
    return

greetings("Samay")
greetings("Pratima")
greetings("Steven")

'''
Function with Return Value
The return keyword as the last statement in function definition indicates end of function block, 
and the program flow goes back to the calling function. Although reduced indent after the last statement 
in the block also implies return but using explicit return is a good practice.
'''
def add(x,y):
   z=x+y
   return z

a=10
b=20
result = add(a,b)
print ("a = {} b = {} a+b = {}".format(a, b, result))


'''
Types of Function Arguments
Based on how the arguments are declared while defining a Python function, they are classified into the following categories −

Positional or required arguments

Keyword arguments

Default arguments

Positional-only arguments

Keyword-only arguments

Arbitrary or variable-length arguments

In the next few chapters, we will discuss these function arguments at length.

Order of Arguments
A function can have arguments of any of the types defined above. However, the arguments must be declared in the following order −

The argument list begins with the positional-only args, followed by the slash (/) symbol.

It is followed by regular positional args that may or may not be called as keyword arguments.

Then there may be one or more args with default values.

Next, arbitrary positional arguments represented by a variable prefixed with single asterisk, that is treated as tuple. It is the next.

If the function has any keyword-only arguments, put an asterisk before their names start. Some of the keyword-only arguments may have a default value.

Last in the bracket is argument with two asterisks ** to accept arbitrary number of keyword arguments.
'''