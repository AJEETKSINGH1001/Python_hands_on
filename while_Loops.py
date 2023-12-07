'''
A while loop statement in Python programming language repeatedly executes a target statement as long
as a given boolean expression is true.
'''

count=0
while count<5:
   count+=1
   print ("Iteration no. {}".format(count))

print ("End of while loop")

#Here is another example of using the while loop
var='0'
while var.isnumeric()==True:
   var=input('enter a number..')
   if var.isnumeric()==True:
      print ("Your input", var)
print ("End of while loop")

#The Infinite Loop

var = 14
while var == 1 : # This constructs an infinite loop
   num = int(input("Enter a number :"))
   print ("You entered: ", num)
print ("Good bye!")