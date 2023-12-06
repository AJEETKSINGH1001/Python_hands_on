'''
Python' bitwise operators are normally used with integer type objects. However, instead of treating the object as a whole, it is treated as a string of bits.
Different operations are done on each bit in the string.
Python has six bitwise operators - &, |, ^, ~, << and >>.
All these operators (except ~) are binary in nature, in the sense they operate on two operands. Each operand is a binary digit (bit) 1 or 0.
'''
'''
When you use integers as the operands, both are converted in equivalent binary, the & operation is done on corresponding bit from each number, 
starting from the least significant bit and going towards most significant bit.
'''

a=60
b=13
print ("a:",a, "b:",b, "a&b:",a&b)

#Bitwise OR Operator (|)
a=60
b=13
print ("a:",a, "b:",b, "a|b:",a|b)
print ("a:", bin(a))
print ("b:", bin(b))

#Python − Binary XOR Operator (^)
#The term XOR stands for exclusive OR. It means
#that the result of OR operation on two bits will be 1 if only one of the bits is 1.
'''
0 ^ 0 is 0
0 ^ 1 is 1
1 ^ 0 is 1
1 ^ 1 is 0
'''
a=60
b=13
print ("a:",a, "b:",b, "a^b:",a^b)

# Binary NOT Operator (~)

a=60
print ("a:",a, "~a:", ~a)

# Left Shift Operator (<<)

a=60
print ("a:",a, "a<<2:", a<<2)

'''
0011 1100
<<
    2
-------------
1111 0000

>>> int('11110000',2)
240
'''
#Right Shift Operator (>>)

a=60
print ("a:",a, "a>>2:", a>>2)

'''
   0011 1100
   >>
   2
   -------------
   0000 1111
   
   >>> int('00001111',2)
15
'''