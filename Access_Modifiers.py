'''
The languages such as C++ and Java, use access modifiers to restrict access to class members (i.e., variables and methods).
These languages have keywords public, protected, and private to specify the type of access.
A class member is said to be public if it can be accessed from anywhere in the program.
Private members are allowed to be accessed from within the class only.
'''

class Employee:
   'Common base class for all employees'
   def __init__(self, name="Bhavana", age=24):
      self.name = name
      self.age = age

e1 = Employee()
e2 = Employee("Bharat", 25)

print ("Name: {}".format(e1.name))
print ("age: {}".format(e1.age))
print ("Name: {}".format(e2.name))
print ("age: {}".format(e2.age))

'''
Python doesn't enforce restrictions on accessing any instance variable or method. However, Python prescribes 
a convention of prefixing name of variable/method with single or double underscore to emulate 
behavior of protected and private access modifiers.
To indicate that an instance variable is private, prefix it with double underscore (such as "__age"). 
To imply that a certain instance variable is protected, prefix it with single underscore (such as "_salary")
'''

class Employee:
   def __init__(self, name, age, salary):
      self.name = name # public variable
      self.__age = age # private variable
      self._salary = salary # protected variable
   def displayEmployee(self):
      print ("Name : ", self.name, ", age: ", self.__age, ", salary: ", self._salary)

e1=Employee("Bhavana", 24, 10000)

print (e1.name)
print (e1._salary)
print (e1.__age)

#Name Mangling
'''
Python doesn't block access to private data, it just leaves for the wisdom of the programmer, 
not to write any code that access it from outside the class. 
You can still access the private members by Python's name mangling technique.
Name mangling is the process of changing name of a member with double underscore to the 
form object._class__variable. If so required, it can still be accessed from outside the class, but the practice should be refrained.
'''

'''
Getters and Setter Methods
A getter method retrieves the value of an instance variable, usually named as get_varname, 
whereas the setter method assigns value to an instance variable − named as set_varname.
Let us define getter methods get_name() and get_age(), and setters set_name() and set_age() in the Employee class.
'''

class Employee:
   def __init__(self, name, age):
      self.__name = name
      self.__age = age

   def get_name(self):
      return self.__name
   def get_age(self):
      return self.__age
   def set_name(self, name):
      self.__name = name
      return
   def set_age(self, age):
      self.__age=age

e1=Employee("Bhavana", 24)
print ("Name:", e1.get_name(), "age:",

e1.get_age())
e1.set_name("Archana")
e1.set_age(21)
print ("Name:", e1.get_name(), "age:", e1.get_age())