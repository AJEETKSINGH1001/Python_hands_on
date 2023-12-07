'''
It terminates the current loop and resumes execution at the next statement, just like the traditional break statement in C.
The most common use for break is when some external condition is triggered requiring a hasty exit from a loop.
The break statement can be used in both while and for loops.
'''

for letter in 'Python':  # First Example
    if letter == 'h':
        break
    print('Current Letter :', letter)

var = 10  # Second Example
while var > 0:
    print('Current variable value :', var)
    var = var - 1
    if var == 5:
        break

print("Good bye!")