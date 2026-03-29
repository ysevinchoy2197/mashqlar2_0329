#1-misol
words = ["apple", "banana", "cherry", "grape", "watermelon"]

result = list(filter(lambda x: len(x) > 5 and 'a' in x, words))

print(result)

#2-misol
students = [
    {"name": "Ali", "grades": [80, 90, 85]},
    {"name": "Vali", "grades": [90, 95, 92]},
    {"name": "Sami", "grades": [70, 75, 72]}
]

best = max(students, key=lambda x: sum(x["grades"]) / len(x["grades"]))

print(best["name"])

#3-misol
from functools import reduce

nums = [1, 2, 3, 4]

result = reduce(lambda x, y: x * y, nums)

print(result)

#4-misol
words = ["apple", "bat", "banana", "cat"]

sorted_words = sorted(words, key=lambda x: (len(x), x))

print(sorted_words)

#5-misol
products = [
    {"name": "phone", "price": 300},
    {"name": "mouse", "price": 50},
    {"name": "keyboard", "price": 120}
]

result = list(map(
    lambda x: x["name"],
    filter(lambda x: x["price"] > 100, products)
))

print(result)
