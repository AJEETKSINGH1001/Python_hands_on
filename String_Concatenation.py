'''
The "+" operator is well-known as an addition operator, returning the sum of two numbers. However, the "+" symbol
acts as string concatenation operator in Python.
It works with two string operands, and results in the concatenation of the two.
'''

str1="Hello"
str2="World"
print ("String 1:",str1)
print ("String 2:",str2)
str3=str1 + str2
print("String 3:",str3)

#insert a whitespace between the two, use a third empty string.
str1="Hello"
str2="World"
blank=" "
print ("String 1:",str1)
print ("String 2:",str2)
str3=str1+blank+str2
print("String 3:",str3)

#The integer operand
#is the number of copies of the string operand to be concatenated.

str1="Hello"
str2="World"
print ("String 1:",str1)
print ("String 2:",str2)
str3=str1+str2*3
print("String 3:",str3)
str4=(str1+str2)*3
print ("String 4:", str4)
