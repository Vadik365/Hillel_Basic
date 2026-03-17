#### 6.1 Діапазон букв ###
import string

all_letters = string.ascii_letters

while True:
    user_inp = input("Enter two letters with hyphen(-): ")

    if user_inp.count("-") != 1:
        print("Error: Please enter only one hyphen")
        continue

    start, end = user_inp.split("-")

    if len(start) != 1 or len(end) != 1:
        print("Error: You must enter two letters")
        continue

    if start not in all_letters or end not in all_letters:
        print("Error: Only letters allowed")
        continue

    start_index = all_letters.index(start)
    end_index = all_letters.index(end)

    if start_index <= end_index:
        print(all_letters[start_index:end_index + 1])
    else:
        print(all_letters[start_index:end_index - 1:-1])
    break

#### 6.2 Конвертер із числа в дату ###
seconds = int(input("Enter seconds: "))
days, remainder = divmod(seconds, 86400)
hours, remainder = divmod(remainder, 3600)
minutes, seconds = divmod(remainder, 60)

if days % 10 == 1 and days % 100 != 11:
    day_word = "день"
elif days % 10 in [2, 3, 4] and days % 100 not in [12, 13, 14]:
    day_word = "дні"
else:
    day_word = "днів"
print(f"{days} {day_word}, {str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}")

#### 6.3 Добуток чисел ###
number = input("Enter number: ")
while  not number.isdigit():
    print("Please enter number")
    number = input("Enter number: ")
number = int(number)
while number > 9:
    result = 1

    for digit in str(number):
        result *= int(digit)
    number = result

print(number)


