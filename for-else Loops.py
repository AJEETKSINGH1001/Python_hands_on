'''
Python supports having an "else" statement associated with a "for" loop statement. If the "else" statement is used with a "for" loop, the "else" statement is executed when the sequence is
exhausted before the control shifts to the main line of execution.
'''

for count in range(6):
   print ("Iteration no. {}".format(count))
else:
   print ("for loop over. Now in else block")
print ("End of for loop")

'''
Nested Loops in Python
Python programming language allows the use of one loop inside another loop. 
The following section shows a few examples to illustrate the concept.
'''

for i in range(1,11):
   for j in range(1,11):
      k=i*j
      print ("{:3d}".format(k), end=' ')
   print()