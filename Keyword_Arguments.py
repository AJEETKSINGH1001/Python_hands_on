'''
Python allows to pass function arguments in the form of keywords which are also called named arguments. Variables in the function definition are used as keywords.
When the function is called, you can explicitly mention the name and its value.
'''

# Function definition is here
def printinfo( name, age ):
   "This prints a passed info into this function"
   print ("Name: ", name)
   print ("Age ", age)
   return

# Now you can call printinfo function
# by positional arguments
printinfo ("Naveen", 29)

# by keyword arguments
printinfo(name="miki", age = 30)

# keyword argument with the help of following function definition −

def division(num, den):
   quotient = num/den
   print ("num:{} den:{} quotient:{}".format(num, den, quotient))

division(10,5)
division(5,10)

#Try to call the division() function with the following statement.
def division(num, den):
   quotient = num/den
   print ("num:{} den:{} quotient:{}".format(num, den, quotient))

#division(num=5, 10)
