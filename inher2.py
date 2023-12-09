class Employee:
   def __init__(self,nm, sal):
      self.name=nm
      self.salary=sal
   def getName(self):
      return self.name
   def getSalary(self):
      return self.salary

class SalesOfficer(Employee):
   def __init__(self,nm, sal, inc):
      super().__init__(nm,sal)
      self.incnt=inc
   def getSalary(self):
      return self.salary+self.incnt

e1=Employee("Rajesh", 9000)
print ("Total salary for {} is Rs {}".format(e1.getName(),e1.getSalary()))
s1=SalesOfficer('Kiran', 10000, 1000)
print ("Total salary for {} is Rs {}".format(s1.getName(),s1.getSalary()))

'''
Sr.No	Method, Description & Sample Call
1

__init__ ( self [,args...] )

Constructor (with any optional arguments)

Sample Call : obj = className(args)

2

__del__( self )

Destructor, deletes an object

Sample Call : del obj

3

__repr__( self )

Evaluatable string representation

Sample Call : repr(obj)

4

__str__( self )

Printable string representation

Sample Call : str(obj)
'''