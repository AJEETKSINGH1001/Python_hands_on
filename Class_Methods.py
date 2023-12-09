'''
Python has a built-in function classmethod() which transforms an instance method
to a class method which can be called with the reference to the class only and not the object.
'''

class Employee:
   empCount = 0
   def __init__(self, name, age):
      self.__name = name
      self.__age = age
      Employee.empCount += 1
   def showcount(self):
         print (self.empCount)
   counter=classmethod(showcount)

e1 = Employee("Bhavana", 24)
e2 = Employee("Rajesh", 26)
e3 = Employee("John", 27)

e1.showcount()
Employee.counter()

'''
Using @classmethod() decorator is the prescribed way to define a class method as it is more convenient than 
first declaring an instance method and then transforming to a class method.
'''


