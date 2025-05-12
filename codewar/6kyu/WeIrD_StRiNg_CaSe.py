'''
Write a function that accepts a string, and returns the same string with all even indexed characters in each word upper cased, 
and all odd indexed characters in each word lower cased. The indexing just explained is zero based, so the zero-ith index is even, 
therefore that character should be upper cased and you need to start over for each word.

The passed in string will only consist of alphabetical characters and spaces(' '). Spaces will only be present if there are multiple words. 
Words will be separated by a single space(' ').


Examples:
"String" => "StRiNg"
"Weird string case" => "WeIrD StRiNg CaSe"

'''

# Input: String
# Output: String
# Function: 

# def to_weird_case(words):
    
#     i = 0
#     new_string = ""
#     for char in words:
#         if char.isspace():
#             new_string += char
#             i = 0
#         else:
#             if i % 2 == 0:
#                 new_string += char.upper()
#             else:
#                 new_string += char.lower()
#             i += 1
#     return new_string

# print(to_weird_case("Weird string case"))


def to_weird_case(words):
    return ' '.join(''.join(c.upper() if i % 2 == 0 else c.lower() 
                    for i, c in enumerate(word)) 
                    for word in words.split())

print(to_weird_case("Weird string case"))


# best practice
'''
def to_weird_case(words):
    return ' '.join(''.join(c.upper() if i % 2 == 0 else c.lower() 
                    for i, c in enumerate(word)) 
                    for word in words.split())
'''