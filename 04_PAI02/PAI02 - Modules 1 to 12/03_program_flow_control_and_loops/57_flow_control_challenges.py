# Create a Python script that asks the user for a number and then prints out a list of all the divisors of each number
# less than the asked number.

x = int(input("Enter a number: "))
all_divisors = list()
for i in range(2, x//2+1):
    if x % i == 0:
        all_divisors.append(i)

print(all_divisors)


# Write a Python program to check if an integer (x) is the power of another integer (y). Prompt the user to input both integers.
# Input: 16, 2
# Output: 4 ** 2 = 16

x = int(input("Enter a number x: "))
y = int(input(f"Enter a number y to test if x which is {x} is a power of y: "))

found = False

for k in range(2, x//2):
    if y ** k == x:
        print(f"{y} ** {k} = {x}")
        found = True
        break
else:
    print(f'{x} is not the power of {y}')


# Write a Python program that counts and displays the vowels of a given string ignoring the case.

vowels = 'aeiou'
my_str = 'Cogito, ergo sum.'

count = 0
for v in vowels:
    if v in my_str.lower():
        count += my_str.count(v)

print(f'Total number of vowels: {count}')


# Write a Python script that checks whether a triangle is equilateral, isosceles, or scalene.
# Prompt the user to enter the lengths of the three sides.
#
# Triangle Types:
#
# Equilateral: All three sides are equal.
#
# Isosceles: Two sides are equal.
#
# Scalene: All sides are different.
#
# Input: Enter the lengths of the triangle sides:
#
# x: 6
#
# y: 8
#
# z: 12
#
# Output: Scalene triangle.

a, b, c = input('Enter the lengths of the triangle sides [Example: 10 20 30]:').split()
a, b, c = float(a), float(b), float(c)
if a == b == c:
    print("Equilateral triangle.")
elif a == b or b == c or a == c:
    print("Isosceles triangle.")
else:
    print("Scalene triangle.")


# Write a Python program that prompts the user for multiple float numbers and calculates:
#
# The sum
#
# The product
#
# The average
#
# Enter 0 to finish.

print("Enter some floats to calculate their sum, product and average. Input 0 to exit.")

count = 0
sum = 0.0
product = 1

while True:
    number = float(input(''))
    if number == 0:
        break
    sum += number
    product *= number
    count += 1
    if count < 2:
        print("Enter at least two numbers.")
    else:
        print(f'Sum, average and product are: {sum}, {sum/count}, {product}')


# Given a string, write a program that calculates the sum and average of all digits in the string, ignoring other characters.
#
# Example:
#
# Input: "Python31py50"
#
# Output: Sum: 9, Average: 2.25

my_str = 'Python31py50'

total, count = 0, 0
for char in my_str:
    if char.isdigit():
        total += int(char)
        count += 1

print(f'Sum: {total}\nAverage: {total/count}')


# Write a Python program that displays the multiplication table (from 1 to 10) for a number entered by the user.

n = int(input("Enter an integer number: "))

for i in range(1,11):
    print(f'{n} x {i} = {n * i}')


# Write a Python script that displays the following pattern from 1 to n where n is entered by the user.

# If the user enters 3 it will display:
#
# 1
# 22
# 333

n = int(input('Enter whole number: '))
for i in range(n + 1):
    print(str(i) * i)


# Write a Python program that finds the common characters that appear in two given strings.

s1 = 'Hello you!'
s2 = 'python'

common_chars = ''
for c1 in s1:
    if c1 in s2:
        if c1 not in common_chars: # adding the common char only once
            common_chars += c1

print(f'Common characters: {common_chars}')


# Write a Python program that iterates through numbers from 1 to 50 and prints:
#
# "Foo" for multiples of 3
#
# "Bar" for multiples of 5
#
# "FooBar" for multiples of both 3 and 5

for i in range(1,51):
    if i % 3 == 0 and i % 5 == 0:
        print('FooBar')
    elif i % 3 == 0:
        print('Foo')
    elif i % 5 == 0:
        print('Bar')
    else:
        print(i)


# Write a Python script that prints out the Fibonacci series up to a given number n.
#
# Fibonacci Series: https://www.mathsisfun.com/numbers/fibonacci-sequence.html
#
# Example: if n is 23 it will print out 0, 1, 1, 2, 3, 5, 8, 13, 21

n = 100
a, b = 0, 1
while a <= n:
    print(a, ' ', end=' ')
    a, b = b, a + b


#
# Write a Python script that draws the following pattern using for loops.
#
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *

n = 10
for i in range(n):
    for _ in range(i):
        print(' *', end='')
    print('')

for j in range(n, 0, -1):
    for _ in range(j):
        print(' *', end='')
    print('')