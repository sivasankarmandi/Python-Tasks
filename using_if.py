# 33. Write a Python program to sum three given integers. However, if two values are equal, the sum will be zero.

# Code :-

def sum_with_condition(a, b, c):
    if a == b or b == c or a == c:
        return 0
    else:
        return a + b +cr
a = int(input("Enter the first integer: "))
b = int(input("Enter the second integer: "))
c = int(input("Enter the third integer: "))
result = sum_with_condition(a, b, c)
print("Sum with condition:", result)