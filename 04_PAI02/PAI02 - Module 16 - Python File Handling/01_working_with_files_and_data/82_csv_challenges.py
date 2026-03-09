# Using Python’s built-in csv module, write each inner list to a CSV file named people1.csv.
# Then read the file and print its contents.
# Use the default comma (,) as the delimiter.

import csv

people = [
    ['Dan', 34, 'Bucuresti'],
    ['Andrei',21, 'London'],
    ['Maria', 45, 'Paris']
]

# writing into a csv file
with open('people1.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    for item in people:
        writer.writerow(item)

# reading a csv file
with open('people1.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)


# Modify the solution from the previous challenge so that the delimiter
# used in the CSV file is a colon (:) instead of a comma.

people = [
    ['Dan', 34, 'Bucuresti'],
    ['Andrei',21, 'London'],
    ['Maria', 45, 'Paris']
]

# writing into a csv file
with open('people2.csv', 'w', newline='') as f:
    writer = csv.writer(f, delimiter=':')
    for item in people:
        writer.writerow(item)


# reading a csv file
with open('people2.csv') as f:
    reader = csv.reader(f, delimiter=':')
    for row in reader:
        print(row)