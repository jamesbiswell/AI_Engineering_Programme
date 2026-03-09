# Range Expressions (Character Classes)
import re

print(re.findall(r'[aeiouAEIOU]', 'Generative AI'))

# Key patterns:
# [abc]
# [A-Z]
# [a-z]
# [0-9] # not [0-10]
# [a-zA-Z]
# [a-zA-Z0-9_] # Combination of letters, digits, and underscore
# [^a-z] # Everything EXCEPT lowercase letters

# [0-9]
numbers = '1,2,3,4,5,a,b,c,d,e'
extracted_numbers = re.findall(r'[0-9]+', numbers)
print(extracted_numbers) # Output: ['1', '2', '3', '4', '5']

# [^a-z]
print(re.findall(r'[^a-z]', 'Hello, World! 123'))

username = 'AI_dev42'
pattern = r'^[a-zA-Z0-9_]+$' # Only letters, digits, and underscore
if re.match(pattern, username) :
    print('Valid Username!')
else:
    print('Invalid Username!')

# [^...] - Carat inside the square brackets instructs regex to match anything EXCEPT the specified characters
text = 'GPT-40, GTP-4o-mini, o1, and o3 are powerful models!'
cleaned_text = re.sub(r'[^a-zA-Z ]', '', text) # Substitute all numeric characters
print(cleaned_text)