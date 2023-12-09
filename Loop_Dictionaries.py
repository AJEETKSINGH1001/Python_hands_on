#Running a simple for loop over the dictionary object traverses the keys used in it.

numbers = {10:"Ten", 20:"Twenty", 30:"Thirty",40:"Forty"}
for x in numbers:
   print (x)

'''
Once we are able to get the key, 
its associated value can be easily accessed either by using square brackets operator or with get() method.
'''

numbers = {10:"Ten", 20:"Twenty", 30:"Thirty",40:"Forty"}
for x in numbers:
   print (x,":",numbers[x])

#The dict_items object is a list of key-value tuples over which a for loop can be run as follows:

numbers = {10:"Ten", 20:"Twenty", 30:"Thirty",40:"Forty"}
for x in numbers.items():
   print (x)

#Here, "x" is the tuple element from the dict_items iterator.
# We can further unpack this tuple in two different variables.

numbers = {10:"Ten", 20:"Twenty", 30:"Thirty",40:"Forty"}
for x,y in numbers.items():
   print (x,":", y)

numbers = {10:"Ten", 20:"Twenty", 30:"Thirty",40:"Forty"}
for x in numbers.keys():
   print (x, ":", numbers[x])

numbers = {10:"Ten", 20:"Twenty", 30:"Thirty",40:"Forty"}
l = len(numbers)
for x in range(l):
   print (list(numbers.keys())[x], ":", list(numbers.values())[x])
