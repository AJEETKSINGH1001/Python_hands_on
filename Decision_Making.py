'''
Python's decision making functionality is in its keywords − if..elif...else. The if
keyword requires a boolean expression, followed by colon symbol.
The colon (:) symbol starts an indented block. The statements with the same level of
indentation are executed if the boolean expression in if statement is True. If the expression is not True (False), the interpreter bypasses the indented block and proceeds to execute statements at earlier indentation level.
'''

discount = 0
amount = 1200

# Check he amount value
if amount > 1000:
   discount = amount * 10 / 100

print("New amount after discount = ", amount - discount)
