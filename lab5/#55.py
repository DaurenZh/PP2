import re

def match_pattern(string):
    pattern = r'a.*b$'
    if re.match(pattern, string):
        return True
    else:
        return False

test_strings = ["ab", "acb", "axxxb", "abbbb", "acbxxb", "abc", "cba"]
for test_string in test_strings:
    print(f"{test_string}: {match_pattern(test_string)}")
