# Write a Python script that removes all occurrences of a given element from a list.

l1 = [1, 2, 1, 1, 2, 3, 1, 5, 3, 5, 1]

# item to remove from the list
n = 1
while n in l1:
    l1.remove(n)

print(l1)


# Create a Python script that removes all the elements of a list that are duplicate.

l1 = [1, 2, 1, 1, 2, 3, 1, 5, 3, 5, 1]
unique_list = []
for item in l1:
    if item not in unique_list:
        unique_list.append(item)

print(unique_list)


# Given the string nums = '10,20,30,40,50', write a Python script that converts it into a list of integers: [10, 20, 30, 40, 50].

nums = '10,20,30,40,50'
nums_list = nums.split(',')
print(nums_list)  # => ['10', '20', '30', '40', '50']

nums1 = [int(n) for n in nums_list]
print(nums1)    # => [10, 20, 30, 40, 50]


# Write a Python script which finds all numbers that are divisible by 7 but are not a multiple of 5, between 1500 and 3200 (both included).
# The numbers obtained should be printed in a comma-separated sequence (csv) on a single line.

nums = list()

for i in range(1500, 3201):
    if i % 7 == 0 and i % 5 != 0:
        nums.append(str(i))

print(','.join(nums))


# Write a program that asks the user for a long string containing multiple words separated by whitespaces.
# Print back to the user the same string with the words in backwards order.

words = input('Enter some words:')
words_list =  words.split(' ')
# print(words_list)
words_reversed = ' '.join(reversed(words_list))
print(words_reversed)


# Write a Python program that accepts a hyphen-separated sequence of words as input and prints
# the words in a hyphen-separated sequence after sorting them alphabetically.

string = input("Enter a hyphen-separated string: ")
words = string.split("-")
sorted_words = sorted(words)
sorted_str = "-".join(sorted_words)
print(sorted_str)


# Write a Python program that takes a sequence of words separated by spaces and prints the words with their letters reversed.
# Do not use list comprehension.

string = input("Enter a few words separated by whitespaces: ")
words = string.split()

# reverse the letters in each word
i = 0
for w in words:
    words[i] = w[::-1]
    i += 1

new_str = ' '.join(words)
print(new_str)


# Modify the previous challenge by using list comprehension instead.

string = input("Enter a few words separated by whitespaces: ")
words = string.split()

# reverse the letters in each word
words = [w[::-1] for w in words]

new_str = ' '.join(words)
print(new_str)


# Consider a list of words (strings). Write a Python script that generates a list of tuples where the first element of the
# tuple is the word in the list and the second element is its length.

words = ['Python', 'Java', 'C++', 'Golang', 'Solidity', 'Bash']

words_and_length = [(w, len(w)) for w in words]

print(words_and_length)