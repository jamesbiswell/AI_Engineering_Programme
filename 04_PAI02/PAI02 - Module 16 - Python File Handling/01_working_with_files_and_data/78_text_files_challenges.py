# Create a Python script that generates a new file containing only unique MAC addresses,
# with each address on a separate line.

with open('macs.txt') as f:
    content = f.read().split()
    # print(content)

    # eliminating duplicates
    content = list(set(content))
    print(content)

# writing to file
with open('mac_unique.txt', 'w', newline='') as f:
    for mac in content:
        f.write(f'{mac}\n')


# Create a Python script that reads a text file into a list,
# then converts the list into a single string containing the entire file content.

with open('sample_file.txt', 'r') as f:
    # reading the file in a list
    content = f.read().splitlines()
    # concatenating the list back into a string
    my_str = '\n'.join(content)
    print(my_str)


# Write a Python script that removes all empty lines,
# including lines that contain only spaces, from a text file.

# reading the file in a list
with open('file.txt') as f:
    content_list = f.readlines()

# create a new list eliminating the elements that are empty strings or contain only spaces
tmp_list = [line for line in content_list if line.strip() != '']
print(tmp_list)

# write to a new file
with open('file_without_blanks.txt', 'w') as f:
    f.write(''.join(tmp_list))


# Create a Python function called tail that reads the last n lines of a text file.
# The function should accept two arguments: the file name and the number of lines to read (n).
# This mimics the behavior of the Linux tail command.
# Example:
# tail('sample_file.txt', 5)

def tail(file, n):
    with open(file, 'r') as f:
        # reading the file in a list
        content = f.read().splitlines()
        # getting the last n elements of the list
        last = content[len(content)-n:]
        # print(last)
        # concateneting the list back into a string
        my_str = '\n'.join(last)
        return my_str

t = tail('sample_file.txt', 3)
print(t)

# Modify the previous solution so that the script automatically refreshes and prints the last n lines of the file every 3 seconds.
# This is similar to the Linux tail -f command.

# import time
#
# while True:
#     t = tail('sample_file.txt', 3)
#     print(t)
#     time.sleep(3)
#     print('')


# Write a Python program to count the number of lines, words, and characters in a text file — similar to the Linux wc command.
# Try to create a reusable function.

def wc(file):
    with open(file, 'r') as f:
        # reading the file into a list
        content = f.read().splitlines()
        print(content)

        lines = len(content)

        words = 0
        for line in content:
            words += len(line.split())

        chars = 0
        for line in content:
            chars += len(list(line))

        return lines, words, chars

print(wc('sample_file.txt'))


# Write a Python program that calculates the net amount in a bank account based on transactions listed in a text file.
# Each transaction is on a separate line, using this format:
#
# D:50 # Deposit
# W:100 # Withdrawal

with open('banking.txt', 'r') as f:
    content = f.read().splitlines()
    # print(content)

    deposit, withdrawal = 0, 0

    for item in content:
        tmp = item.split(':')
        # print(tmp) # -> ['D', '300']
        if  tmp[0] == 'D':
            deposit += int(tmp[1])
        elif tmp[0] == 'W':
            withdrawal += int(tmp[1])
        else:
            print('File format error')

    balance = deposit - withdrawal
    print(balance)


# Write a Python script that compares two text files line by line and displays only the lines that differ.

with open('a.txt') as f:
    file1 = f.read().splitlines()

with open('b.txt') as f:
    file2 = f.read().splitlines()

file = list(zip(file1, file2))
print(file)

i = 0
for item in file:
    i += 1
    if item[0] != item[1]:
        print(f'file1 ({i}): {item[0]}, file2 ({i}): {item[1]}')


# Write a Python script that reads the english.txt file into a dictionary,
# where each word becomes a key and the length of the word becomes the corresponding value.

with open('english.txt') as f:
    words = f.read().splitlines()

    words_and_length = dict()
    for w in words:
        words_and_length[w] = len(w)

    for k, v in words_and_length.items():
        print(f'{k} -> {v}')


# Using the dictionary created in the previous challenge,
# write a Python script that finds the first 100 longest words in the file.

with open('english.txt') as f:
    words = f.read().splitlines()

    words_and_length = dict()
    for w in words:
        words_and_length[w] = len(w)

    print(words_and_length)
    words_list = sorted(words_and_length.items(), key=lambda x:x[1], reverse=True)
    print(words_list[:100])


# Write a Python script that counts the occurrence of each letter (A-Z, a-z) in all the words of the english.txt file
# Make a distinction between lowercase and uppercase letters.
# At the end, identify:
#
# a) The most frequently used letter in the english.txt file
# b) The least frequently used letter in the english.txt file

import string

letters = dict()

# initializing the dictionary with all letters as keys and zero as values
for c in string.ascii_letters:
    letters[c] = 0

with open('english.txt', 'r') as words:
    for w in words:
        for char in string.ascii_letters:
            letters[char] += w.count(char)

print(letters)


# Update the previous solution so that the script ignores case — all letters should be counted as lowercase.

import string

letters = dict()

# initializing the dictionary with all letters as keys and zero as values
for c in string.ascii_lowercase:
    letters[c] = 0

with open('english.txt', 'r') as words:
    for w in words:
        for char in string.ascii_lowercase:
            letters[char] += w.lower().count(char)  # work on a lowercase copy of w

print(letters)


# Extend the previous challenge to find the three most frequently used letters across all the words in the english.txt file.

import string

letters = dict()

# initializing the dictionary with all letters as keys and zero as values
for c in string.ascii_lowercase:
    letters[c] = 0

with open('english.txt', 'r') as words:
    for w in words:
        for char in string.ascii_lowercase:
            letters[char] += w.count(char)

print(sorted(letters.items(), key=lambda a:a[1], reverse=True)[:3])