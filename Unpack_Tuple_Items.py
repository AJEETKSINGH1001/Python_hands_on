'''
The term "unpacking" refers to the process of parsing tuple items in individual variables. In Python,
the parentheses are the default delimiters for a literal representation of sequence object.
'''

#To store tuple items in individual variables, use multiple variables on the left of assignment operator

tup1 = (10,20,30)
x, y, z = tup1
print ("x: ", x, "y: ", "z: ",z)

tup1 = (10,20,30)
x, *y = tup1
print ("x: ", "y: ", y)

#the tuple contains 6 values and variables to be unpacked are 3. We prefix "*" to the second variable

tup1 = (10,20,30, 40, 50, 60)
x, *y, z = tup1
print ("x: ",x, "y: ", y, "z: ", z)

#What if we add "*" to the first variable?

tup1 = (10,20,30, 40, 50, 60)
*x, y, z = tup1
print ("x: ",x, "y: ", y, "z: ", z)