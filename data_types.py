'''Numeric - int, float, complex
String - str
Sequence - list, tuple, range
Binary - bytes, bytearray, memoryview
Mapping - dict
Boolean - bool
Set - set, frozenset
None - NoneType
'''

#Python Numeric Data Type

var1 = 1       # int data type
var2 = True    # bool data type
var3 = 10.023  # float data type
var4 = 10+3j   # complex data type

print(var1)
print(type(var3))

########################################
'''int (signed integers)
bool (subtype of integers.)
float (floating point real values)
complex (complex numbers)'''

########################################
# integer variable.
a=100
print("The type of variable having value", a, " is ", type(a))

# boolean variable.
b=True
print("The type of variable having value", b, " is ", type(b))

# float variable.
c=20.345
print("The type of variable having value", c, " is ", type(c))

# complex variable.
d=10+3j
print("The type of variable having value", d, " is ", type(d))

'''Sequence is a collection data type. It is an ordered collection of items. 
Items in the sequence have a positional index starting with 0. It is conceptually 
similar to an array in C or C++. 
There are following three sequence data types defined in Python.'''
############################################################################
#String example

str = 'Hello World!'

print (str)          # Prints complete string
print (str[0])       # Prints first character of the string
print (str[2:5])     # Prints characters starting from 3rd to 5th
print (str[2:])      # Prints string starting from 3rd character
print (str * 2)      # Prints string two times
print (str + "TEST") # Prints concatenated string

##################################################
#List
list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']

print (list)            # Prints complete list
print (list[0])         # Prints first element of the list
print (list[1:3])       # Prints elements starting from 2nd till 3rd
print (list[2:])        # Prints elements starting from 3rd element
print (tinylist * 2)    # Prints list two times
print (list + tinylist) # Prints concatenated lists

################################################

'''The main differences between lists and tuples are: Lists are enclosed in brackets ( [ ] ) and their elements and size can be changed
 .ie lists are mutable, while tuples are enclosed in parentheses ( ( ) ) and cannot be updated (immutable). 
Tuples can be thought of as read-only lists. For example −'''

tuple = ( 'abcd', 786 , 2.23, 'john', 70.2  )
tinytuple = (123, 'john')

print (tuple)               # Prints the complete tuple
print (tuple[0])            # Prints first element of the tuple
print (tuple[1:3])          # Prints elements of the tuple starting from 2nd till 3rd
print (tuple[2:])           # Prints elements of the tuple starting from 3rd element
print (tinytuple * 2)       # Prints the contents of the tuple twice
print (tuple + tinytuple)   # Prints concatenated tuples

#Updating the list/Tuple

tuple = ( 'abcd', 786 , 2.23, 'john', 70.2  )
list = [ 'abcd', 786 , 2.23, 'john', 70.2  ]
list[2] = 1000     # Valid syntax with list
tuple[2] = 1000    # Invalid syntax with tuple



