'''
The continue statement in Python returns the control to the beginning of the current loop.
When encountered, the loop starts next iteration without executing the remaining statements in the current iteration.
The continue statement can be used in both while and for loops.
'''

for letter in 'Python': # First Example
   if letter == 'h':
      continue
   print ('Current Letter :', letter)
var = 10 # Second Example
while var > 0:
   var = var -1
   if var == 5:
      continue
   print ('Current variable value :', var)
print ("Good bye!")

#Checking Prime Factors

num = 60
print ("Prime factors for: ", num)
d=2
while num > 1:
   if num%d==0:
      print (d)
      num=num/d
      continue
   d=d+1