'''
Along with the if statement, else keyword can also be optionally used.
It provides an alternate block of statements to be executed if the Boolean expression (in if statement)
is not true. this flowchart shows how else block is used.
'''
age=25
print ("age: ", age)
if age >=18:
   print ("eligible to vote")
else:
   print ("not eligible to vote")


#else if Statement

amount = 2500
print('Amount = ',amount)
if amount > 10000:
   discount = amount * 20 / 100
else:
   if amount > 5000:
      discount = amount * 10 / 100
   else:
      if amount > 1000:
         discount = amount * 5 / 100
      else:
         discount = 0

print('Payable amount = ',amount - discount)


#elif Statement

amount = 5001
print('Amount = ',amount)
if amount > 10000:
   discount = amount * 20 / 100
elif amount > 5000:
   discount = amount * 10 / 100
elif amount > 1000:
   discount = amount * 5 / 100
else:
   discount=0

print('Payable amount = ',amount - discount)

'''
There may be a situation when you want to check for another condition after a condition resolves to true. 
In such a situation, you can use the nested if construct.
'''
# Nested if else

num=8
print ("num = ",num)
if num%2==0:
   if num%3==0:
      print ("Divisible by 3 and 2")
   else:
      print ("divisible by 2 not divisible by 3")
else:
   if num%3==0:
      print ("divisible by 3 not divisible by 2")
   else:
      print ("not Divisible by 2 not divisible by 3")
