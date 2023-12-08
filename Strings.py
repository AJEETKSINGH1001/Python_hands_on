'''
 a string is an immutable sequence of Unicode characters.
 Each character has a unique numeric value as per the UNICODE standard.
 But, the sequence as a whole, doesn't have any numeric value even if all the characters are digits.
 To differentiate the string from numbers and other identifiers, the sequence of characters is included within single,
 double or triple quotes in its literal representation.
'''

var = "Welcome To TutorialsPoint"
print (type(var))

var = 'Welcome to "Python Tutorial" from TutorialsPoint'
print ("var:", var)

var = "Welcome to 'Python Tutorial' from TutorialsPoint"
print ("var:", var)


var = '''
Welcome To
Python Tutorial
from TutorialsPoint
'''
print ("var:", var)

