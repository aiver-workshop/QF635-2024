"""
We can use break point to look at call stacks
Put a break point in cook() method to look at call stacks i.e. prior methods that lead to this method call
"""


def cook():
    chop()
    print("cooking")


def chop():
    # put a break point at the following line
    print("chopping")


def dinner():
    print("dining")
    cook()


# entry method
dinner()
