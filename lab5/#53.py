import re

def find_lowercase_with_underscore(string):
    pattern = r'[a-z]+_[a-z]+'
    matches = re.findall(pattern, string)
    return matches

test_string = "This_is_a_test_smth"
sequences = find_lowercase_with_underscore(test_string)
print("Sequences found:")
for sequence in sequences:
    print(sequence)
