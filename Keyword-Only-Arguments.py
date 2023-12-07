'''
You can use the variables in formal argument list as keywords to pass value.
Use of keyword arguments is optional. But, you can force the function be given arguments by keyword only.
You should put an astreisk (*) before the keyword-only arguments list.
'''

print ("Hello", "World", sep="-")

#The sep argument is keyword-only. Try using it as non-keyword argument.
print ("Hello", "World", "-")

def intr(amt,*, rate):
   val = amt*rate/100
   return val
interest = intr(1000, rate=10)
print(interest)