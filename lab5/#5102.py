import re

def insert_spaces(string):
    modified_string = re.sub(r'([a-z])([A-Z])', r'\1 \2', string)
    return modified_string

string = "ThisIsAString"
new_string = insert_spaces(string)
print("Original string:", string)
print("New string:", new_string)
