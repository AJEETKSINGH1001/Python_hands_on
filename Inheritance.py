'''
Inheritance is one of the most important features of Object-oriented programming methodology.
It is most often used in software development process using many languages such as Java, PHP, Python, etc.
Instead of starting from scratch, you can create a class by deriving it from a pre-existing
class by listing the parent class in parentheses after the new class name.

class SubClassName (ParentClass1[, ParentClass2, ...]):
   'Optional class documentation string'
   class_suite
'''


class Parent:  # define parent class
    def __init__(self):
        self.attr = 100
        print("Calling parent constructor")

    def parentMethod(self):
        print('Calling parent method')

    def set_attr(self, attr):
        self.attr = attr

    def get_attr(self):
        print("Parent attribute :", self.attr)


class Child(Parent):  # define child class
    def __init__(self):
        print("Calling child constructor")

    def childMethod(self):
        print('Calling child method')


c = Child()  # instance of child
c.childMethod()  # child calls its method
c.parentMethod()  # calls parent's method
c.set_attr(200)  # again call parent's method
c.get_attr()  # again call parent's method


#Multiple Inheritance
'''
class parent1:
   #statements
   
class parent2:
   #statements
   
class child(parent1, parent2):
   #statements
'''


class division:
    def __init__(self, a, b):
        self.n = a
        self.d = b

    def divide(self):
        return self.n / self.d


class modulus:
    def __init__(self, a, b):
        self.n = a
        self.d = b

    def mod_divide(self):
        return self.n % self.d


def div_mod(param, param1):
    pass


class div_mod(division, modulus):
    def __init__(self, a, b):
        self.n = a
        self.d = b

    def div_and_mod(self):
        divval = division.divide(self)
        modval = modulus.mod_divide(self)
        return (divval, modval)

    x = div_mod(10, 3)
    print("division:", x.divide())
    print("mod_division:", x.mod_divide())
    print("divmod:", x.div_and_mod())


    