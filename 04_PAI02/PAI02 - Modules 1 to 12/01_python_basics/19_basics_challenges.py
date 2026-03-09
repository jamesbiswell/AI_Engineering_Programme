# Declare variables for the following types: int, float, bool, string, list.
# Print out the variables and their types.

year = 2026  # int
price = 99.99  # float
is_available = True  # bool
product_name = "Laptop"  # string
features = ["Touchscreen", "Backlit Keyboard", "SSD"]  # list

print(type(year), year)
print(type(price), price)
print(type(is_available), is_available)
print(type(product_name), product_name)
print(type(features), features)


# Refactored code following PEP 8 naming and style conventions

# snake_case notation
var_one= 10
var_two= 20

# This is
# an example of a multiline
# comment in Python.

my_str = 'Hello'
print(my_str)


# Fix syntax errors so the script runs without errors

best_friend = 'Anne'
print('My best friend is', best_friend)

age = 18
print(age == 10)

my_value = 15

a, b = '10', '20'
print(a + b)

print('To comment a line of code you put # at the beginning of the line.')


# Using different Python operators

x = 10
y = 3

result1 = x == y  # Equality
result2 = x >= y  # Greater than or equal
result3 = x * y  # Multiplication
result4 = x ** y  # Exponentiation
result5 = x / y  # Division (float)
result6 = x // y  # Floor division
result7 = x % y  # Modulus

x += 5  # Increment x by 5
y *= 2  # Multiply y by 2

print(result1, result2, result3, result4, result5, result6, result7)
print(x, y)


# Given the expression: a = 16 / 2 + 6 / 2 ** 2
# Modify it by adding parentheses to change the order of operations so that a equals 1.0.

a = 16 / ((2 + 6) / 2)**2
print(a)


# Calculate total IPv6 addresses (2^128)

total_ipv6_addresses = 2 ** 128
print(total_ipv6_addresses)