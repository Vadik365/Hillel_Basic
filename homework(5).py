### 5.1 Ім'я змінної ###
import string
import keyword

variable =  str(input("Enter variable name: "))

if variable == "":
    print(False)
elif variable in keyword.kwlist:
    print(False)
elif variable[0].isdigit():
    print(False)
elif variable.count("_") == len(variable) and len(variable) > 1:
    print(False)
else:
    is_valid = True
    for char in variable:
        if char.isupper():
            is_valid = False
        elif char == " ":
            is_valid = False
        elif char in string.punctuation and char != "_":
            is_valid = False
    print(is_valid)
### 5.2. Модифікувати калькулятор ###
answer = "yes"

while answer == "yes":
    num1 = float(input("Enter number #1: "))
    operation = input("Enter operation (+, -, *, /): ")
    num2 = float(input("Enter number #2: "))

    match operation:
        case "+":
            print("Result:", num1 + num2)
        case "-":
            print("Result:", num1 - num2)
        case "*":
            print("Result:", num1 * num2)
        case "/":
            if num2 != 0:
                print("Result:", num1 / num2)
            else:
                print("Cannot divide by zero!")
        case _:
            print("Error: invalid operation!")

    answer = input("Do you want to continue? Yes/No: ").lower()

print("Thank you")

### 5.3. hashtag ###

import string

custom_str = str(input("Enter words for hashtag: "))
words = custom_str.split()
hashtag = "#".capitalize()

for word in words:
    clean_word = ""

    for char in word:
        if char not in string.punctuation:
            clean_word += char
    if clean_word:
        hashtag += clean_word.capitalize()
hashtag = hashtag[:140]
print(hashtag)
