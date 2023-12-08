'''
The function annotation feature of Python enables you to add additional explanatory
metada about the arguments declared in a function definition, and also the return data type.
'''


def myfunction(a: int, b: int):
    c = a + b
    return c

print(myfunction(10, 20))
print(myfunction("Hello ", "Python"))

def myfunction(*args: "arbitrary args", **kwargs: "arbitrary keyword args") -> int:
   pass
print (myfunction.__annotations__)