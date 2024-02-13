#1
def squares_generator(N):
    for i in range(N):
        yield i ** 2
#2
def even_numbers_up_to_N(N):
    for i in range(N + 1):
        if i % 2 == 0:
            yield i

n = int(input("Enter a number: "))
even_nums = even_numbers_up_to_N(n)
print(','.join(map(str, even_nums)))
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
