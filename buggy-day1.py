### Fixed Python
import random

a = random.randint(1, 12)
b = random.randint(1, 12)
for i in range(1):
    question = "What is " + str(a) + " x " + str(b) + "? "
    answer = input(question)
    if answer == str(a * b):
        print("Well done!")
    else:
        print("No.")
