'''
In Python, a string becomes a raw string if it is prefixed with "r" or "R" before the quotation symbols.
Hence 'Hello' is a normal string whereas r'Hello' is a raw string.
'''

# ignore \
s = 'This string will not include \
backslashes or newline characters.'
print (s)

# escape backslash
s=s = 'The \\character is called backslash'
print (s)

# escape single quote
s='Hello \'Python\''
print (s)

# escape double quote
s="Hello \"Python\""
print (s)

# escape \b to generate ASCII backspace
s='Hel\blo'
print (s)

# ASCII Bell character
s='Hello\a'
print (s)

# newline
s='Hello\nPython'
print (s)

# Horizontal tab
s='Hello\tPython'
print (s)

# form feed
s= "hello\fworld"
print (s)

# Octal notation
s="\101"
print(s)

# Hexadecimal notation
s="\x41"
print (s)