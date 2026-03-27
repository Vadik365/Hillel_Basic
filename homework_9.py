#### 9.1. Визначити популярність певних слів у тексті ####
def popular_words (text, words):
    text = text.lower().split()
    popular_words = {}
    for word in words:
        popular_words[word] = text.count(word)
    return popular_words

assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''', ['i', 'was', 'three', 'near']) == { 'i': 4, 'was': 3, 'three': 0, 'near': 0 }, 'Test1'
print('Ok')

#### 9.2. Різниця між числами ####
def difference(*args):
    if not args:
        return 0
    return round(max(args) - min(args), 2)

assert difference(1, 2, 3) == 2, 'Test1'
assert difference(5, -5) == 10, 'Test2'
assert difference(10.2, -2.2, 0, 1.1, 0.5) == 12.4, 'Test3'
assert difference() == 0, 'Test4'
print('Ok')
