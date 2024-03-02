#1
from functools import reduce
from operator import mul
a = int(input())
nums = [int(input()) for i in range(a)]
print(reduce(mul, nums))
#2
def count_upper_lower(string):
    lower_count = 0
    upper_count = 0
    for i in string:
      if(i.islower()):
            lower_count+=1
      else:
            upper_count+=1
    return upper_count, lower_count
input_string = input("Enter a string: ")
upper_count, lower_count = count_upper_lower(input_string)
print(upper_count)
print(lower_count)
#3
def is_palindrome(string):
    string = string.lower()
    string = ''.join(string.split())
    return string == string[::-1]
input_string = input("Enter a string: ")
if is_palindrome(input_string):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
#4
import time
import math
def square_root_after_milliseconds(number, milliseconds):
    time.sleep(milliseconds / 1000)
    result = math.sqrt(number)
    return result
number = 25100
milliseconds = 2123
result = square_root_after_milliseconds(number, milliseconds)
print(f"Square root of {number} after {milliseconds} milliseconds is {result}.")
#5
def all_elem_true(my_tuple):
    res = all(my_tuple)
    return res
my_tuple = (True, True)
my_tuple2 = (False, True)
print(all_elem_true(my_tuple))
print(all_elem_true(my_tuple2))