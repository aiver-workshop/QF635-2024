"""
Debug your first Python application with breakpoints.

Learn the following techniques:
    - Set breakpoints
    - Stepped through your program
    - Created a watch
    - Evaluated an expression

"""

a = 1
total = 0

while a <= 10:
    b = a * a
    total = total + b
    a = a + 1

print('total is {}'.format(total))
