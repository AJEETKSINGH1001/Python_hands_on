'''
In Python, a string is an ordered sequence of Unicode characters.
Each character in the string has a unique index in the sequence.
The index starts with 0. First character in the string has its positional index 0.
The index keeps incrementing towards the end of string
'''

#var="HELLO PYTHON"
#var[7]="y"
#print (var)

var="HELLO PYTHON"

print ("var:",var)
print ("var[3:8]:", var[3:8])

var="HELLO PYTHON"
print ("var:",var)
print ("var[3:8]:", var[3:8])
print ("var[-9:-4]:", var[-9:-4])

var="HELLO PYTHON"
print ("var:",var)
print ("var[0:5]:", var[0:5])
print ("var[:5]:", var[:5])

'''
Similarly, y operand is also optional. By default, it is "-1",
which means the string will be sliced from the xth position up to the end of string.
'''
var="HELLO PYTHON"
print ("var:",var)
print ("var[6:12]:", var[6:12])
print ("var[6:]:", var[6:])