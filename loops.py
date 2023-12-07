#For loop Using "for" with a Tuple

numbers = (34,54,67,21,78,97,45,44,80,19)
total = 0
for num in numbers:
   total+=num
print ("Total =", total)

#Using "for" with a List
numbers = [34,54,67,21,78,97,45,44,80,19]
total = 0
for num in numbers:
   if num%2 == 0:
      print (num)


#Range

numbers = range(5)
'''
start is 0 by default,
step is 1 by default,
range generated from 0 to 4
'''
print (list(numbers))
# step is 1 by default, range generated from 10 to 19
numbers = range(10,20)
print (list(numbers))
# range generated from 1 to 10 increment by step of 2
numbers = range(1, 10, 2)
print (list(numbers))

#Once we obtain the range, we can use the for loop with it.
for num in range(5):
 print (num, end=' ')
print()
for num in range(10,20):
 print (num, end=' ')
print()
for num in range(1, 10, 2):
 print (num, end=' ')

 #Factorial of a Number
 '''
 Factorial is a product of all numbers from 1 to that number say n. 
 It can also be defined as product of 1, 2, up to n.
 Factorial of a number n! = 1 * 2 * . . . . . * n
 '''
 fact = 1
 N = 5
 for x in range(1, N + 1):
    fact = fact * x
 print("factorial of {} is {}".format(N, fact))

#We can then form a for loop as follows:
numbers = [34,54,67,21,78]
indices = range(len(numbers))
for index in indices:
   print ("index:",index, "number:",numbers[index])

#Running a simple for loop over the dictionary object traverses the keys used in it.

numbers = {10:"Ten", 20:"Twenty", 30:"Thirty",40:"Forty"}
for x in numbers:
   print (x)


#Once we are able to get the key, its associated value can be easily accessed either by
# using square brackets operator or with the get() method.
# Take a look at the following example

numbers = {10:"Ten", 20:"Twenty", 30:"Thirty",40:"Forty"}
for x in numbers:
   print (x,":",numbers[x])

'''
The items(), keys() and values() methods of dict class return the view objects dict_items, 
dict_keys and dict_values respectively. 
These objects are iterators, and hence we can run a for loop over them.
'''
numbers = {10:"Ten", 20:"Twenty", 30:"Thirty",40:"Forty"}
for x in numbers.items():
   print (x)

#"x" is the tuple element from the dict_items iterator.
# We can further unpack this tuple in two different variables. Check the following code −

numbers = {10:"Ten", 20:"Twenty", 30:"Thirty",40:"Forty"}
for x,y in numbers.items():
   print (x,":", y)
