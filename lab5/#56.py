import re

def replace_with_colon(text):
    pattern = r'[ ,.]'
    replaced_text = re.sub(pattern, ':', text)
    return replaced_text

text = "This is a test, it has some spaces."
replaced_text = replace_with_colon(text)
print("Original text:", text)
print("Text with replaced characters:", replaced_text)
