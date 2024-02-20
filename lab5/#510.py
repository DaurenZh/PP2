import re
def camel_to_snake(camel_case):
    snake_case = ''
    for char in camel_case:
        if char.isupper():
            snake_case += '_' + char.lower()
        else:
            snake_case += char
    return snake_case

camel_string = "convertThisCamelCaseString"
snake_string = camel_to_snake(camel_string)
print("Camel Case:", camel_string)
print("Snake Case:", snake_string)
