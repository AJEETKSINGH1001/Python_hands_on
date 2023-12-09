'''
Abstraction is one of the important principles of object-oriented programming.
It refers to a programming approach by which only the relevant data about an object is exposed, hiding all the other details.
This approach helps in reducing the complexity and increasing the efficiency in application development.
'''

from abc import ABC, abstractmethod


class democlass(ABC):
    @abstractmethod
    def method1(self):
        print("abstract method")
        return

    def method2(self):
        print("concrete method")


class concreteclass(democlass):
    def method1(self):
        super().method1()
        return


obj = concreteclass()
obj.method1()
obj.method2()