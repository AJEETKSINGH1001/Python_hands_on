'''
Types of Operators
Python language supports the following types of operators −

Arithmetic Operators

Comparison (Relational) Operators

Assignment Operators

Logical Operators

Bitwise Operators

Membership Operators

Identity Operators

Operator Precedence in Python
In Python, an expression contains one or variables, literals and operators (arithmetic, logical, binary etc.).
Python interpreter evaluates the expression and the result is either assigned to a variable
or used in another statement. Interpreter performs various operations according to the precedence of operators.
If a certain expression contains multiple operators, their order of evaluation is
determined by the order of precedence. For example, consider the following expression.
If we consider only the arithmetic operators in Python, the traditional BODMAS rule is also employed by Python interpreter, where the brackets are evaluated first, the division and multiplication operators next, followed by addition and subtraction operators.
Hence, a will become 17 in the above expression.

'''


a = 20
b = 10
c = 15
d = 5
e = 0

e = (a + b) * c / d       #( 30 * 15 ) / 5
print ("Value of (a + b) * c / d is ",  e)

e = ((a + b) * c) / d     # (30 * 15 ) / 5
print ("Value of ((a + b) * c) / d is ",  e)

e = (a + b) * (c / d);    # (30) * (15/5)
print ("Value of (a + b) * (c / d) is ",  e)

e = a + (b * c) / d;      #  20 + (150/5)
print ("Value of a + (b * c) / d is ",  e)

#Python − Addition Operator (+)

a=10
b=20
print ("Addition of two integers")
print ("a =",a,"b =",b,"addition =",a+b)

#Addition of integer and float results in a float.
a=10
b=20.5
print ("Addition of integer and float")
print ("a =",a,"b =",b,"addition =",a+b)

#The result of adding float to complex is a complex number.

a=10+5j
b=20.5
print ("Addition of complex and float")
print ("a=",a,"b=",b,"addition=",a+b)

#Python − Subtraction Operator (-)

a=10
b=20
print ("Subtraction of two integers:")
print ("a =",a,"b =",b,"a-b =",a-b)
print ("a =",a,"b =",b,"b-a =",b-a)

#Subtraction of an integer and a float follows the same principle.
a=10
b=20.5
print ("subtraction of integer and float")
print ("a=",a,"b=",b,"a-b=",a-b)
print ("a=",a,"b=",b,"b-a=",b-a)

#In the subtraction involving a complex and a float,
# real component is involved in the operation.
a=10+5j
b=20.5
print ("subtraction of complex and float")
print ("a=",a,"b=",b,"a-b=",a-b)
print ("a=",a,"b=",b,"b-a=",b-a)

#Python − Multiplication Operator (*)

a=10
b=20
print ("Multiplication of two integers")
print ("a =",a,"b =",b,"a*b =",a*b)

#In multiplication, a float operand may have a standard decimal point notation, or a scientific notation.

a=10
b=20.5
print ("Multiplication of integer and float")
print ("a=",a,"b=",b,"a*b=",a*b)

a=-5.55
b=6.75E-3
print ("Multiplication of float and float")
print ("a =",a,"b =",b,"a*b =",a*b)


#For the multiplication operation involving one complex operand,
# the other operand multiplies both the real part and imaginary part

a=10+5j
b=20.5
print ("Multiplication of complex and float")
print ("a =",a,"b =",b,"a*b =",a*b)

#Python − Division Operator (/)

a=10
b=20
print ("Division of two integers")
print ("a=",a,"b=",b,"a/b=",a/b)
print ("a=",a,"b=",b,"b/a=",b/a)

#In Division, a float operand may have a standard decimal point notation,
# or a scientific notation.
a=10
b=-20.5
print ("Division of integer and float")
print ("a=",a,"b=",b,"a/b=",a/b)
a=-2.50
b=1.25E2
print ("Division of float and float")
print ("a=",a,"b=",b,"a/b=",a/b)

'''
When one of the operands is a complex number, division between the other 
operand and both parts of complex number (real and imaginary) object takes place.
'''
a=7.5+7.5j
b=2.5
print ("Division of complex and float")
print ("a =",a,"b =",b,"a/b =",a/b)
print ("a =",a,"b =",b,"b/a =",b/a)

#Python − Modulus Operator (%)

a=10
b=2
print ("a=",a, "b=",b, "a%b=", a%b)
a=10
b=4
print ("a=",a, "b=",b, "a%b=", a%b)
print ("a=",a, "b=",b, "b%a=", b%a)
a=0
b=10
print ("a=",a, "b=",b, "a%b=", a%b)
print ("a=", a, "b=", b, "b%a=",b%a)


