'''
Python's Unicode Support
Python 3.0 onwards has built-in support for Unicode.
The str type contains Unicode characters, hence any string created using single,
double or the triple-quoted string syntax is stored as Unicode.
The default encoding for Python source code is UTF-8.
Hence, string may contain literal representation of a Unicode character (3/4) or
its Unicode value (\u00BE).
'''

var = "3/4"
print (var)
var = "\u00BE"
print (var)

################################################

'''
In the following example, a string '10' is stored using 
the Unicode values of 1 and 0 which are \u0031 and u0030 respectively.
'''

var = "\u0031\u0030"
print (var)

################################################
'''
In the following example, we have a string variable that consists of ASCII characters. 
ASCII is a subset of Unicode character set.
The encode() method is used to convert it into a bytes object.
'''

string = "Hello"
tobytes = string.encode('utf-8')
print (tobytes)
string = tobytes.decode('utf-8')
print (string)

###################################################
'''
the Rupee symbol (₹) is stored in the variable using its Unicode value. 
We convert the string to bytes and back to str.
'''
string = "\u20B9"
print (string)
tobytes = string.encode('utf-8')
print (tobytes)
string = tobytes.decode('utf-8')
print (string)

####################################################


