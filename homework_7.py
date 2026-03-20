#### 7.1. Вітання ####
def say_hi(name, age):
  return f"Hi. My name is {name} and I'm {age} years old"

assert say_hi("Alex", 32) == "Hi. My name is Alex and I'm 32 years old", 'Test1'
print(say_hi("Alex", 32))
assert say_hi("Frank", 68) == "Hi. My name is Frank and I'm 68 years old", 'Test2'
print(say_hi("Frank", 68))
print("Ok")

#### 7.2. Модифікувати рядок ####
def correct_sentence(text):
    text = text[0].upper() + text[1:]

    if not text.endswith("."):
        text += "."

    return text

assert correct_sentence("greetings, friends") == "Greetings, friends.", 'Test1'
assert correct_sentence("hello") == "Hello.", 'Test2'
assert correct_sentence("Greetings. Friends") == "Greetings. Friends.", 'Test3'
assert correct_sentence("Greetings, friends.") == "Greetings, friends.", 'Test4'
assert correct_sentence("greetings, friends.") == "Greetings, friends.", 'Test5'
print("Оk")

#### 7.3 Пошук підрядка ####
def second_index(text, some_str):

    first = text.find(some_str)
    if first == -1:
        return None

    second = text.find(some_str, first +1)
    if second == -1:
        return None

    return second


assert second_index("sims", "s") == 3, 'Test1'
assert second_index("find the river", "e") == 12, 'Test2'
assert second_index("hi", "h") is None, 'Test3'
assert second_index("Hello, hello", "lo") == 10, 'Test4'
print("Ok")

#### ДЗ 7.4. Пошук спільних елементів ####
def common_elements():
    list_3 = set(range(0, 100, 3))
    list_5 = set(range(0, 100, 5))
    return list_3.intersection(list_5)


assert common_elements() == {0, 75, 45, 15, 90, 60, 30}
print("Ok")