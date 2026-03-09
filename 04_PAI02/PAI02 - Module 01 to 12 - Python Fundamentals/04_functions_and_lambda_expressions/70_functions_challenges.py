# Write a Python function that takes a list as an argument and returns a new list with unique
# elements of the first list in the same order.
from asyncio import print_call_graph

def unique_list(my_list):
    tmp_list = list()
    for x in my_list:
        if x not in tmp_list:
            tmp_list.append(x)
    return tmp_list

friends = ['Dan', 'Maria', 'Dan', 'Dan', 'John', 'Dan']
print(unique_list(friends))


# Write a Python function to check whether a number is perfect or not.
# The function should return True if the number is perfect and False otherwise.
# Perfect numbers: https://www.britannica.com/science/perfect-number

def all_divisors(n):
    """
     This function returns all divisors of a number
    """
    divisors = []
    for x in range(1, int(n/2)+1):
        if n % x == 0:
            divisors.append(x)
    return divisors

def perfect_number(n):
    divs = all_divisors(n)
    if sum(divs) == n:
        return True
    else:
        return False

# calling the function
n = 496
if perfect_number(n):
    print(f'{n} is a rare kind of number, as it\'s a perfect number')
else:
    print(f'Nothing special about {n}, it\'s not a perfect number')


# Write a Python function that takes an integer n as an argument and returns its factorial.
# Learn more about factorials: Factorial – Wikipedia
def fact(n):
    if n < 0:
        print('The function\'s argument (n) should be greater than or equal to zero.')
    elif n == 0:
        return 1
    else:
        f = 1
        while n > 0:
            f *= n
            n -= 1
            print(f)
        return f

y = 10
print(f'The factorial of {y} is {fact(y)}')


# Create a function that takes an integer as an argument and returns True if it’s a prime number and False otherwise.

def is_prime(n):
    prime = True
    if n == 1: # 1 is not a prime number, the first prime number is 2
        return False
    i = 1
    while i < n // 2:
        i = i + 1
        if n % i == 0:
            prime = False
            break
    return prime # returns True or False

print(is_prime(11))


# Find 5 prime numbers greater than 1,000,000

primes = []
for n in range(1_000_000, 100_000_000):
   if is_prime(n):
       primes.append(n)
       if len(primes) == 5:
           break

print(primes)


# Write a function called fibo that takes an integer greater than 10
# and returns the Fibonacci sequence from 0 up to (but not exceeding) the given number.
# https://www.mathsisfun.com/numbers/fibonacci-sequence.html

def fibo(n):
    if n <= 10:
        print('The function\'s argument (n) should be greater than 10.')
    else:
        a, b = 0, 1
        fibo_list = []
        while a <= n:
            fibo_list.append(a)
            a, b = b, a + b
        return fibo_list

print(fibo(100))


# Write a function that takes in a list as an argument and returns the Equilibrium Index of the list.
# If there isn't such an index it returns False.
# Equilibrium index: https://www.geeksforgeeks.org/equilibrium-index-of-an-array/

def equilibrium_index(my_list):
    for x in range(0,len(my_list)):
        if sum(my_list[:x]) == sum(my_list[x+1:]):
            return x
    return False

nums = [2, 3, 10, 5]
print(equilibrium_index(nums))  # => 2

nums = [3, 3, 10, 5]
print(equilibrium_index(nums))  # => False


# Write a function that takes in a csv string as an argument and returns the Equilibrium Index of the numbers in the csv string.
# If there isn't such an index it returns False.
# Equilibrium index: https://www.geeksforgeeks.org/equilibrium-index-of-an-array/

def equilibrium_index(my_str):
    my_list = my_str.split(',')   # => string to list
    my_list = [int(n) for n in my_list]  # => converting the list of strings to a list of ints

    for x in range(0,len(my_list)):
        if sum(my_list[:x]) == sum(my_list[x+1:]):
            return x
    return False

nums = '2, 3, 10, 5'
print(equilibrium_index(nums))  # => 2

nums = '3, 3, 10, 5'
print(equilibrium_index(nums))  # => False


# Define a function to draw a Christmas tree with a given height, for example:
#         *
#        ***
#       *****
#      *******
#     *********

def draw_tree(height):
  # Loop through each row of the tree
  for i in range(1, height + 1):
    # Print the spaces before the asterisks on each row
    for j in range(height - i):
      print(" ", end="")
    # Print the asterisks on each row
    for j in range(2 * i - 1):
      print("*", end="")
    # Move to the next line
    print()

# Call the function to draw a tree with a height of 10
draw_tree(10)