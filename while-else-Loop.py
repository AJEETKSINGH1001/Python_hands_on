'''
Python supports having an else statement associated with a while loop statement.
If the else statement is used with a while loop, the else statement is executed when
the condition becomes false before the control shifts to the main line of execution.
'''

count=0
while count<5:
   count+=1
   print ("Iteration no. {}".format(count))
else:
   print ("While loop over. Now in else block")
print ("End of while loop")