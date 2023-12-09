'''
According to principle of data encapsulation, the data members that describe an object are hidden
from environment that is external to class. They are available for processing to methods defined within the
class only. Methods themselves on the other hand are accessible from outside class context. Hence object data is said to be encapsulated by the methods.
The result of such encapsulation is that any unwarranted access to the object data is prevented.
'''

class Student:
   def __init__(self, name="Rajaram", marks=50):
      self.name = name
      self.marks = marks

s1 = Student()
s2 = Student("Bharat", 25)

print ("Name: {} marks: {}".format(s1.name, s2.marks))
print ("Name: {} marks: {}".format(s2.name, s2.marks))