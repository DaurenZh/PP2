import re

def match_pattern(string):
    pattern = r'^a.*b$' # . - some char, $ - end, ^ - starts with
    if re.match(pattern, string): # re.match checks if the pattern matches at the beginning 
        return True
    else:
        return False

test_strings = ["ab", "acb", "axxxb", "abbbb", "acbxxb", "abc", "cba"]
for test_string in test_strings:
    print(f"{test_string}: {match_pattern(test_string)}")
