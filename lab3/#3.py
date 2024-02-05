import math
import random
#Classes1
class StringManipulator:
    def getString(self):
        self.input_string = input("Enter a string: ")

    def printString(self):
        print("String in upper case:", self.input_string.upper())

stringManipulator = StringManipulator()    
stringManipulator.getString()
stringManipulator.printString()
#Classes2
class Shape:
    def __init__(self):
        pass

    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        super().__init__()
        self.length = length

    def area(self):
        return self.length * self.length

shape = Shape()
square = Square(4)
print("Area of the generic Shape:", shape.area())
print("Area of the Square:", square.area())
#Classes3
class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
rectangle = Rectangle(int(input()), int(input()))
print("Area of the Rectangle:", rectangle.area())
#Classes4
class Point: #model for a point in two-dimensional space
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def show(self):
        print(f"Coordinates: ({self.x}, {self.y})")

    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def dist(self, other_point):
        return math.sqrt((self.x - other_point.x)**2 + (self.y - other_point.y)**2)
point1 = Point(1, 2)
point2 = Point(4, 6)
point1.show()
point1.move(3, 5)
point1.show()
distance = point1.dist(point2)
print(f"Distance between point1 and point2: {distance}")
#Classes5
class Account:
    def __init__(self, owner, initial_balance=0):
        self.owner = owner
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")
my_account = Account(owner="John Doe", initial_balance=1000)
my_account.deposit(500)
my_account.deposit(200)
my_account.withdraw(300)
my_account.withdraw(1000) 
print(f"Balance for {my_account.owner}: {my_account.balance}")
#Classes6
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
a = int(input())
nums = [int(input()) for i in range(a)]
prime_nums = list(filter(lambda x: is_prime(x), nums))
print("Original list:", nums)
print("Prime numbers:", prime_nums)
#Functions1.1
def grams_to_ounces(grams):
    ounces = 28.3495231 * grams
    return ounces
grams_value = 500
ounces_result = grams_to_ounces(grams_value)
print(f"{grams_value} grams is equal to {ounces_result:.2f} ounces.")
#Functions1.2
def fahrenheit_to_celsius(fahrenheit):
    celsius = (5 / 9) * (fahrenheit - 32)
    return celsius
fahrenheit_temperature = float(input("Enter Fahrenheit temperature: "))
celsius_temperature = fahrenheit_to_celsius(fahrenheit_temperature)
print(f"{fahrenheit_temperature} degrees Fahrenheit is equal to {celsius_temperature:.2f} degrees Celsius.")
#Functions1.3
def solve(numheads, numlegs):
    for x in range(numheads + 1):
        y = numheads - x  # Calculate the number of rabbits
        if (2 * x + 4 * y) == numlegs:
            return x, y
    return None
numheads = int(input())
numlegs = int(input())
result = solve(numheads, numlegs)
if result:
    chickens, rabbits = result
    print(f"Number of chickens: {chickens}")
    print(f"Number of rabbits: {rabbits}")
else:
    print("No solution found.")
#Functions1.4
def filter_prime(arr):
    primes = []
    for num in arr:
        if num < 2:
            continue
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num%i==0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes
a = int(input())
arr = [int(input()) for i in range(a)]
prime_numbers = filter_prime(arr)
print(prime_numbers)
#Functions1.5
def print_permutations_recursive(current_str, remaining_chars):
    if not remaining_chars:
        print(current_str)
        return
    for i in range(len(remaining_chars)):
        new_current = current_str + remaining_chars[i]
        new_remaining = remaining_chars[:i] + remaining_chars[i + 1:]
        print_permutations_recursive(new_current, new_remaining)
def print_permutations_from_user_input():
    user_input = input("Enter a string: ")
    print("All permutations:")
    print_permutations_recursive("", user_input)
print_permutations_from_user_input()
#Functions1.6
def reverse_word(input_str):
    words = input_str.split()
    reversed_sentence = " ".join(reversed(words))
    return reversed_sentence
input = input("Enter a sentence: ")
result = reverse_word(input)
print("Reversed words:", result)
#Functions1.7
def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False
print(has_33([1, 3, 3]))      
print(has_33([1, 3, 1, 3]))    
print(has_33([3, 1, 3]))  
#Functions1.8
def spy_game(nums):
    pos_1 = pos_2 = pos_3 = None
    for i, num in enumerate(nums):
        if num == 0:
            if pos_1 is None:
                pos_1 = i
            elif pos_2 is None:
                pos_2 = i
        elif num == 7:
            pos_3 = i
    return pos_1 is not None and pos_2 is not None and pos_3 is not None and pos_1 < pos_2 < pos_3

print(spy_game([1,2,4,0,0,7,5]))  # True
print(spy_game([1,0,2,4,0,5,7]))  # True
print(spy_game([1,7,2,0,4,5,0]))  # False
#Functions1.9
def volume_sphere(radius):
    v = (4/3)*3,14*(radius**3)
    return v
r = int(input())
print(volume_sphere(r))
#Functions1.10
def unique_elements(input_list):
    unique_list = []
    
    for item in input_list:
        if item not in unique_list:
            unique_list.append(item)
    
    return unique_list
a = int(input())
arr = [int(input()) for i in range(a)]
result = unique_elements(arr)
print(result)
#Functions1.11
def is_palindrome(s):
    return s == s[::-1]
print(is_palindrome("madam"))
#Functions1.12
def print_histogram(numbers):
    for num in numbers:
        print('*' * num)
print_histogram([4, 9, 7])
#Functions1.13
def guess_the_number():
    print("Hello! What is your name?")
    player = input()
    print(f"Well, {player}, I am thinking of a number between 1 and 20.")
    secret = random.randint(1, 20)
    guesses = 0
    while True:
        print("Take a guess.")
        guess = int(input())
        guesses += 1
        if guess == secret:
            print(f"Good job, {player}! You guessed my number in {guesses} guesses!")
            break
        elif guess < secret:
            print("Your guess is too low.")
        else:
            print("Your guess is too high.")
guess_the_number()
#Functions1.14





