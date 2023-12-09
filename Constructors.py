'''
A constructor is an instance method in a class, that is automatically called whenever a new object of the class is declared. The constructor' role is to assign value to instance variables as soon as the object is declared.
Python uses a special method called __init__() to initialize the instance variables for the object, as soon as it is declared.
The __init__() method acts as a constructor. It needs a mandatory argument self, which the reference to the object.
The __init__() method as well as any instance method in a class has a mandatory parameter, self.
However, you can give any name to the first parameter, not necessarily self.
'''

class Employee:
   'Common base class for all employees'
   def __init__(self):
      self.name = "Bhavana"
      self.age = 24

e1 = Employee()
print ("Name: {}".format(e1.name))
print ("age: {}".format(e1.age))

#Parameterized Constructor

class Employee:
   'Common base class for all employees'
   def __init__(self, name, age):
      self.name = name
      self.age = age

e1 = Employee("Bhavana", 24)
e2 = Employee("Bharat", 25)

print ("Name: {}".format(e1.name))
print ("age: {}".format(e1.age))
print ("Name: {}".format(e2.name))
print ("age: {}".format(e2.age))

#You can assign defaults to the formal arguments in the constructor so
# that the object can be instantiated with or without passing parameters.

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
Python - Instance Methods
In addition to the __init__() constructor, there may be one or more instance methods defined in a class. 
A method with self as one of the formal arguments is called instance method, 
as it is called by a specific object.
'''

class Employee:
   def __init__(self, name="Bhavana", age=24):
      self.name = name
      self.age = age
   def displayEmployee(self):
      print ("Name : ", self.name, ", age: ", self.age)

e1 = Employee()
e2 = Employee("Bharat", 25)

e1.displayEmployee()
e2.displayEmployee()

'''
The getattr(obj, name[, default]) − to access the attribute of object.

The hasattr(obj,name) − to check if an attribute exists or not.

The setattr(obj,name,value) − to set an attribute. If attribute does not exist, then it would be created.

The delattr(obj, name) − to delete an attribute.
'''

