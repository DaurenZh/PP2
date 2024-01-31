 
#this is 2lab full solutions

#Booleans1
print(10>9)
#False

#Booleans2
print(10==9)
#False

#Booleans3
print(10<9)
#False

#Booleans4
print(bool("abc"))
#True

#Booleans5
print(bool(0))
#False

#Operators1
print(10*9)

#Operators2
print(10/2)

#Operators3
fruits = ["apple", "banana"]
if "apple" in fruits:
  print("Yes, apple is a fruit!")

#Operators4
if 5!=10:
  print("5 and 10 is not equal")

#Operators5
if 5 == 10 or 4 == 4:
  print("At least one of the statements is true")

#Lists1
fruits = ["apple", "banana", "cherry"]
print(fruits[1])

#Lists2
fruits = ["apple", "banana", "cherry"]
fruits[0] = "kiwi"

#Lists3
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")

#Lists4
fruits = ["apple", "banana", "cherry"]
fruits.insert(1, "lemon")

#Lists5
fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")

#Lists6
fruits = ["apple", "banana", "cherry"]
print(fruits[-1])

#Lists7
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits[2:5])

#Lists8
fruits = ["apple", "banana", "cherry"]
print(len(fruits))

#Tuples1
fruits = ("apple", "banana", "cherry")
print(fruits[0])

#Tuples2
fruits = ("apple", "banana", "cherry")
print(len(fruits))

#Tuples3
fruits = ("apple", "banana", "cherry")
print(fruits[-1])

#Tuples4
fruits = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(fruits[2:5])

#Sets1
fruits = {"apple", "banana", "cherry"}
if "apple" in fruits:
  print("Yes, apple is a fruit!")

#Sets2
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")

#Sets3
fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits)

#Sets4
fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")

#Sets5
fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")

#Dictionaries1
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(car.get("model"))

#Dictionaries2
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["year"] = 2020

#Dictionaries3
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["color"] = "red"

#Dictionaries4
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.pop("model")

#Dictionaries5
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.clear()

#If...Else1
a = 50
b = 10
if a > b:
 print("Hello World")

#If...Else2
a = 50
b = 10
if a != b:
  print("Hello World")

#If...Else3
a = 50
b = 10
if a == b:
  print("Yes")
else:
  print("No")

#If...Else4
a = 50
b = 10
if a == b:
  print("1")
elif a > b:
  print("2")
else:
  print("3")

#If...Else5
c = d = 0
if a == b and c == d:
  print("Hello")

#If...Else6
if a == b or c == d:
  print("Hello")

#If...Else7
if 5 > 2:
    print("YES")

#If...Else8
a = 2
b = 5
print("YES") if a == b else print("NO")

#If...Else9
a = 2
b = 50
c = 2
if a == c or b == c:
  print("YES")

#WhileLoops1
i = 1
while i < 6:
  print(i)
  i += 1

#WhileLoops2
i = 1
while i < 6:
  if i == 3:
    break
  i += 1

#WhileLoops3
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

#WhileLoops4
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")

#ForLoops1
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

#ForLoops2
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

#ForLoops3
for x in range(6):
  print(x)

#ForLoops4
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)