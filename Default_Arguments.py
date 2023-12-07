'''
Python allows to define a function with default value assigned to one or more formal arguments.
Python uses the default value for such an argument if no value is passed to it. If any value is passed,
the default value is overridden with the actual value passed.
'''

# Function definition is here
def printinfo( name, age = 35 ):
   "This prints a passed info into this function"
   print ("Name: ", name)
   print ("Age ", age)
   return

# Now you can call printinfo function
printinfo( age=50, name="miki" )
printinfo( name="miki" )

#Defsult argumrnt

def percent(phy, maths, maxmarks=200):
   val = (phy+maths)*100/maxmarks
   return val

phy = 60
maths = 70
result = percent(phy,maths)
print ("percentage:", result)

phy = 40
maths = 46
result = percent(phy,maths, 100)
print ("percentage:", result)