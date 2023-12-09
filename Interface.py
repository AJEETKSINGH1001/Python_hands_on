'''
interface is a software architectural pattern. An interface is like a class but its methods just have prototype signature definition without any body to implement. The recommended functionality needs to be implemented by a concrete class.
In languages like Java, there is interface keyword which makes it easy to define an interface. Python doesn't have it or any similar keyword. Hence the same ABC class and @abstractmethod decorator is used as done in an abstract class.
An abstract class and interface appear similar in Python. The only difference in two is that the abstract class may have some non-abstract methods, while all methods in interface must be abstract,
and the implementing class must override all the abstract methods.
'''

from abc import ABC, abstractmethod
class demoInterface(ABC):
   @abstractmethod
   def method1(self):
      print ("Abstract method1")
      return

   @abstractmethod
   def method2(self):
      print ("Abstract method1")
      return

#This is test

class concreteclass(demoInterface):
    def method1(self):
        print("This is method1")
        return

    def method2(self):
        print("This is method2")
        return


obj = concreteclass()
obj.method1()
obj.method2()