'''
Python literals or constants are the notation for representing a fixed value in source code.
In contrast to variables, literals (123, 4.3, "Hello") are static values or you can say constants which do not change throughout the operation of the program or application.
For example, in the following assignment statement.
'''

##################################################
# Using Octal notation
x = 0O34
print ("0O34 in octal is", x, type(x))
# Using Hexadecimal notation
x = 0X1c
print ("0X1c in Hexadecimal is", x, type(x))

####################################################

'''
Python - Float Literal
A floating point number consists of an integral part and a fractional part. Conventionally, a decimal point symbol (.) 
separates these two parts in a literal representation of a float. For example,
'''
# Using normal floating point notation
x = 1.23
print ("1.23 in normal float literal is", x, type(x))
# Using Scientific notation
x = 1.23E5
print ("1.23E5 in scientific notation is", x, type(x))
x = 1.23E-2
print ("1.23E-2 in scientific notation is", x, type(x))

############################################################
'''
Python - Complex Literal
A complex number comprises of a real and imaginary component. 

The imaginary component is any number (integer or floating point) multiplied by square root of "-1"

(√ −1). In literal representation (−1−−−√
) is representation by "j" or "J". Hence, a literal representation of a complex number takes a form x+yj.
'''
#Using literal notation of complex number
x = 2+3j
print ("2+3j complex literal is", x, type(x))
y = 2.5+4.6j
print ("2.5+4.6j complex literal is", y , type(y))

######################################################
'''
Python - String Literal
A string object is one of the sequence data types in Python. It is an immutable sequence of Unicode code points. 
Code point is a number corresponding to a character according to Unicode standard. 
Strings are objects of Python's built-in class 'str'.
String literals are written by enclosing a sequence of characters 
in single quotes ('hello'), double quotes ("hello") or triple quotes (' or """hello""").
'''
var1='hello'
print ("'hello' in single quotes is:", var1, type(var1))
var2="hello"
print ('"hello" in double quotes is:', var1, type(var1))
var3='''hello'''
print ("''''hello'''' in triple quotes is:", var1, type(var1))
var4="""hello"""
print ('"""hello""" in triple quotes is:', var1, type(var1))

####################################################

var1='Welcome to "Python Tutorial" from TutorialsPoint'
print (var1)
var2="Welcome to 'Python Tutorial' from TutorialsPoint"
print (var2)

#####################################################
L1=[1,"Ravi",75.50, True]
print (L1, type(L1))

#Python - Tuple Literal

T1=(1,"Ravi",75.50, True)
print (T1, type(T1))

'''
imp
Default delimiter for Python sequence is parentheses, which means 
a comma separated sequence without parentheses also amounts to declaration of a tuple.
'''

T1=1,"Ravi",75.50, True
print (T1, type(T1))

#Python - Dictionary Literal

capitals={"USA":"New York", "France":"Paris", "Japan":"Tokyo",
"India":"New Delhi"}
numbers={1:"one", 2:"Two", 3:"three",4:"four"}
points={"p1":(10,10), "p2":(20,20)}

print (capitals, type(capitals))
print (numbers, type(numbers))
print (points, type(points))




