import re

def find_uppercase_lowercase_sequence(string):
    pattern = r'[A-Z][a-z]+'
    matches = re.findall(pattern, string)
    return matches

test_string = "TestString"
sequences = find_uppercase_lowercase_sequence(test_string)
print("Sequences found:")
for sequence in sequences:
    print(sequence)
