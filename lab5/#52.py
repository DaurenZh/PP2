import re

def match_pattern(string):
    pattern = r'ab{2,3}'
    if re.fullmatch(pattern, string):
        return True
    else:
        return False

test_strings = ["ab", "aab", "abb", "aabb", "abbbbb", "ac", "abc", "cba"]
for test_string in test_strings:
    print(f"{test_string}: {match_pattern(test_string)}")
