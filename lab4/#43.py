#1
def squares_generator(N):
    for i in range(N):
        yield i ** 2
#2
def even_numbers(N):
    for i in range(N + 1):
        if i % 2 == 0:
            yield i

n = int(input("Enter a number: "))
list_of_nums = [int(input) for i in range(n)]
for i in even_numbers(list_of_nums):
    print (i, end = " ")
#3
def divisible_by_3_and_4(start, end):
    for i in range(start, end + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i
#4
def squares(a, b):
    for i in range(a, b + 1):
        yield i ** 2
a = int(input())
b = int(input())
for square in squares(a, b):
    print(square)
#5
def countdown(n):
    while n >= 0:
        yield n
        n -= 1
n = int(input())
for num in countdown(n):
    print(num)
