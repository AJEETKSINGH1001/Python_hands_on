'''
Packages in Python extend the concept of modular approach further. Package is a folder containing one or
more module files; additionally a special file "__init__.py" file which may
be empty but may contain the package list.
'''

#testpackage.py
from mypackage import power, circle

print ("Area of circle:", circle(5))
print ("10 raised to 2:", power(10,2))