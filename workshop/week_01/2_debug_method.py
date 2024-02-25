"""
Use breakpoints to walk through and understand codes:
    1. Put a few breakpoints inside the main and method(). Use "step over" button to study the code line by line.
    2. Look at the values of `nums` under the Variable panel.
    3. Observe how value of variables such as `a`, `b` and `i` are changing.
    4. Highlight some codes such as `all(a)`, right click and try "evaluate expression" to get the result.
    5. Add comments to document the function.

"""


# what does this method do?
def mysterious_method(nums: [float]) -> bool:
    a = []
    b = []
    for i in range(len(nums) - 1):
        a.append(nums[i] <= nums[i + 1])
        b.append(nums[i] >= nums[i + 1])

    return all(a) or all(b)


if __name__ == '__main__':
    x = [6, 5, 4, 4]
    y = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
    z = [1, 1, 2, 3, 7]

    result_x = mysterious_method(x)
    result_y = mysterious_method(y)
    result_z = mysterious_method(z)

    print(result_x)
    print(result_y)
    print(result_z)
