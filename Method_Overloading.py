'''
When you have a class with method of one name defined more than one but with different
argument types and/or return type, it is a case of method overloading.
Python doesn't support this mechanism as the following code shows
 Python doesn't support this mechanism as the following code shows −
'''

class example:
   def add(self, a, b):
      x = a+b
      return x
   def add(self, a, b, c):
      x = a+b+c
      return x

obj = example()

print (obj.add(10,20,30))
#print (obj.add(10,20))

'''
To simulate method overloading, we can use a workaround by defining default value to method arguments as None, 
so that it can be used with one, two or three arguments.
'''

class example:
   def add(self, a = None, b = None, c = None):
      x=0
      if a !=None and b != None and c != None:
         x = a+b+c
      elif a !=None and b != None and c == None:
         x = a+b
      return x

obj = example()

print (obj.add(10,20,30))
print (obj.add(10,20))

'''
Python's standard library doesn't have any other provision for implementing method overloading. 
However, we can use dispatch function from a third party module named MultipleDispatch for this purpose.
First, you need to install the Multipledispatch module.

pip install multipledispatch

This module has a @dispatch decorator. It takes the number of arguments to be passed to the method to be overloaded. Define multiple copies of add() method with @dispatch decorator as below 
'''

from multipledispatch import dispatch
class example:
   @dispatch(int, int)
   def add(self, a, b):
      x = a+b
      return x
   @dispatch(int, int, int)
   def add(self, a, b, c):
      x = a+b+c
      return x

obj = example()

print (obj.add(10,20,30))
print (obj.add(10,20))



