'''
Python Explicit Casting
Although automatic or implicit casting is limited to int to float conversion, you can use Python's built-in functions int(), float() and str() to perform the explicit conversions such as string to integer.

Python int() Function
Python's built-in int() function converts an integer literal to an integer object, a float to integer, and a string to integer if the string itself has a valid integer literal representation.

Using int() with an int object as argument is equivalent to declaring an int object directly.
'''

a = int(1)     # a will be 1
b = int(2.2)   # b will be 2
c = int("3")   # c will be 3

print (a)
print (b)
print (c)

###########################################
'''
Python float() Function
The float() is a built-in function in Python. 
It returns a float object if the argument is a float literal, 
integer or a string with valid floating point representation.
Using float() with an float object as argument is equivalent to 
declaring a float object directly
'''
a = float(1)     # a will be 1.0
b = float(2.2)   # b will be 2.2
c = float("3.3") # c will be 3.3

print (a)
print (b)
print (c)

############################################################
'''
Python str() Function
We saw how a Python obtains integer or float number from corresponding string representation.
The str() function works the opposite. It surrounds an integer or a float object with quotes (') to return a str object. The str() function returns the string representation of any Python object. 
In this section, we shall see different examples of str() function in Python.
'''

a = str(1)     # a will be "1"
b = str(2.2)   # b will be "2.2"
c = str("3.3") # c will be "3.3"

print (a)
print (b)
print (c)

print(type(a))
print(type(b))
print(type(c))
###############################################
'''
Conversion of Sequence Types
List, Tuple and String are Python's sequence types. They are ordered or indexed collection of items.
A string and tuple can be converted into a list object by using the list() function. Similarly, 
the tuple() function converts a string or list to a tuple.
We shall take an object each of these three sequence types and study their inter-conversion.
'''




