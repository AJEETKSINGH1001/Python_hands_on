'''
All the arguments are required

The number of actual arguments must be equal to the number of formal arguments.

Formal arguments are positional. They Pick up values in the order of definition.

The type of arguments must match.

Names of formal and actual arguments need not be same.
'''

def add(x,y):
   z=x+y
   print ("x={} y={} x+y={}".format(x,y,z))

a=10
b=20
add(a,b)