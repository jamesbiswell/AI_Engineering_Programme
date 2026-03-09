# Calculate company's profit from revenue

revenue = 45_897_513
profit_percentage = 12.7 / 100
profit = revenue * profit_percentage

# Display profit with 2 decimal places
print(f'Company\'s profit: ${profit:.2f}')


# Consider the following string declaration which is part of the output of a Linux command.
my_str = 'wlo1      Link encap:Ethernet  HWaddr b4:6d:83:77:85:f3'
# Write a Python script that extracts the MAC address (b4:6d:83:77:85:f3) from the string.
# Try to solve the challenge in more than one way.

# SOLUTION 1
mac = my_str[len(my_str)-17:]
print(mac)      # => b4:6d:83:77:85:f3

# SOLUTION 2
mac = my_str[-1:-18:-1]
mac = mac[::-1]     # reverse the string
print(mac)          # => b4:6d:83:77:85:f3

# SOLUTION 3
# Split the string into a list and return the last list element which is the MAC address
mac = my_str.split()[-1]
print(mac)     # => b4:6d:83:77:85:f3


# Display the following strings literally:

message = "It displayed: \"You've got an error!\""
print(message)
# or
message = 'It displayed: "You\'ve got an error!"'
print(message)

print('\\n means a new line.')
# or
print(r'\n means a new line')  # r'' means a raw string where \ doesn't have a special meaning.

print('\\ is known as the escape character.')


# Write a Python script that converts foot [ft] to centimeter [cm]. 1 ft = 30.48 cm
# The user will be prompted to enter the value in ft.
# Display the value in cm with 2 decimals, formatted using an f-string.

ft = float(input('Enter distance (in ft):'))
cm = ft * 30.48
print(f'{ft} ft = {cm:.2f} cm')


# Write a Python script that tests if a string is a palindrome.
# https://en.wikipedia.org/wiki/Palindrome

s1 = 'mom'
print(f'Is s1 palindrome? => {s1 == s1[::-1]}')

s2 = 'eve'
print(f'Is s2 palindrome? => {s2 == s2[::-1]}')

s3 = 'Daddy'
print(f'Is s3 palindrome? => {s3 == s3[::-1]}')


# Write a Python script that tests if a string is a palindrome, ignoring whitespace.
# https://en.wikipedia.org/wiki/Palindrome

s4 = 'Rats live on no evil star'
s4 = s4.replace(' ', '')
s4 = s4.lower()
print(f'Is s4 palindrome? => {s4 == s4[::-1]}')

s5 = 'Able was I ere I saw Elba'
s5 = s5.replace(' ', '')
s5 = s5.lower()
print(f'Is s5 palindrome? => {s5 == s5[::-1]}')

s6 = 'Go hang a salami Im a   lasagna hog'
s6 = s6.replace(' ', '')
s6 = s6.lower()
print(f'Is s6 palindrome? => {s6 == s6[::-1]}')


# Write a Python script to get a string made of the first 2 and the last 2 chars from a given string entered by the user.

my_str = input('Enter a string(min 2 chars):')
new_str = my_str[:2] + my_str[-2:]
print(new_str)


# Write a Python script that replaces all occurrences of the first character in a string with '$', except for the first occurrence itself.

my_str = input('Enter a string:')
char = my_str[0]
new_str = my_str[1:].replace(char, '$')
new_str = char + new_str
print(new_str)


# Write a Python program to remove the nth index character from a non-empty string.

n = int(input('Enter the nth index char to remove:'))
my_str = input('Enter the string to change:')
first_part = my_str[0:n]
last_part = my_str[n+1:]
new_str = first_part + last_part
print(new_str)


# Write a Python script to remove the characters which have odd index values of a given string.

my_str = input('Enter the string to change:')
new_str = my_str[::2]
print(new_str)


# Write a Python script that prompts the user for the radius of a circle and calculates its area.
# Circle's area = pi * r ** 2 where pi = 3.1415
# Using an f-string display the area of the circle with 4 decimal places.

radius = float(input('Enter circle radius:'))
area = 3.1415 * radius ** 2
print(f'The area of a circle with a radius of {radius} is {area:.4f}')


# Write a Python script that finds all occurrences of a substring in a given string by ignoring the letter case.

my_str = "Welcome to Romania. romania is an awesome country, isn't it? Hello roMania!"
sub_string = "Romania"

# convert string to lowercase
tmp_str = my_str.lower()

# use the count function
count = tmp_str.count(sub_string.lower())
print(f'The substring "Romania" appears {count} times in the string.')


# Write a Python script that displays a number with a comma (,) as the thousands separator (US and UK format)
# and with a period(.) as the thousands separator (EU format).

n = 12384756982
n_comma = f'{n:,}'

print(n_comma)

print(n_comma.replace(',','.'))
