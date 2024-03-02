import re

def match_pattern(string):
    pattern = r'ab*' # * - means >=0
    if re.fullmatch(pattern, string): #re.fullmatch() if every element coincide
        return True
    else:
        return False

test_strings = ["ab", "aab", "abb", "aabb", "abbbbb", "ac", "abc", "cba"]
for test_string in test_strings:
    print(f"{test_string}: {match_pattern(test_string)}") 
