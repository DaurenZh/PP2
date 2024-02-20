import re

def split_at_uppercase(string):
    parts = re.findall('[A-Z][^A-Z]*', string)
    return parts

string = "SplitThisStringAtUppercaseLetters"
parts = split_at_uppercase(string)
print("Original string:", string)
print("After splitting:", parts)
