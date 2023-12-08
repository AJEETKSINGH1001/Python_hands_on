'''
You may want to define a function that is able to accept arbitrary or variable number of arguments. Moreover, the arbitrary number of arguments might be positional or keyword arguments.

An argument prefixed with a single asterisk * for arbitrary positional arguments.

An argument prefixed with two asterisks ** for arbitrary keyword arguments.
'''

# sum of numbers
def add(*args):
   s=0
   for x in args:
      s=s+x
   return s
result = add(10,20,30,40)
print (result)

result = add(1,2,3)
print (result)


# avg of first test and best of following tests
def avg(first, *rest):
    second = max(rest)
    return (first + second) / 2


result = avg(40, 30, 50, 25)
print(result)

'''
The addr() function has an argument **kwargs which is able to accept any number of address elements like name, city, phno, pin, etc. Inside the function kwargs 
dictionary of kw:value pairs is traversed using items() method.
'''

def addr(**kwargs):
   for k,v in kwargs.items():
      print ("{}:{}".format(k,v))

print ("pass two keyword args")
addr(Name="John", City="Mumbai")
print ("pass four keyword args")

# pass four keyword args
addr(Name="Raam", City="Mumbai", ph_no="9123134567", PIN="400001")

'''
percent() function where marks in science and marks are stored in required arguments,
and the marks in variable number of elective subjects in **optional argument
'''
def percent(math, sci, **optional):
   print ("maths:", math)
   print ("sci:", sci)
   s=math+sci
   for k,v in optional.items():
      print ("{}:{}".format(k,v))
      s=s+v
   return s/(len(optional)+2)

result=percent(math=80, sci=75, Eng=70, Hist=65, Geo=72)
print ("percentage:", result)
