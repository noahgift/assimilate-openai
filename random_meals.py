import random

fruits = ["apple", "banana", "orange", "pear", "pineapple", "strawberry", "watermelon"]
dishes = ["pizza", "pasta", "burger", "steak", "salad", "soup", "chicken"]

meals = []

for i in range(5):
    meals.append(random.choice(fruits) + " " + random.choice(dishes))

print(meals)