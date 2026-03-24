#### 8.1. Додати 1 до числа ####
def add_one(some_list):
    nums = ''.join(map(str, some_list))
    num = int(nums) + 1
    return list(map(int, str(num)))
assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
assert add_one([0]) == [1], 'Test3'
assert add_one([9]) == [1, 0], 'Test4'
print("Оk")

#### 8.2. Паліандром ####
def is_palindrome(text):
    palindrome = ""
    for char in text.lower():
        if char.isalnum():
            palindrome += char
    return palindrome == palindrome[::-1]
assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
print("Оk")

#### 8.3. Унікальне число ####
def find_unique_value(some_list):
   for num in some_list:
       if some_list.count(num) == 1:
           return num
assert find_unique_value([1, 2, 1, 1]) == 2, 'Test1'
assert find_unique_value([2, 3, 3, 3, 5, 5]) == 2, 'Test2'
assert find_unique_value([5, 5, 5, 2, 2, 0.5]) == 0.5, 'Test3'
print("Оk")