calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(string):
    count_calls()
    return len(string), string.upper(), string.lower()


def is_contains (string, list_to_search):
    count_calls()
    string_lower = string.lower()
    return string_lower in (item.lower() for item in list_to_search)


print(string_info('Hello, world!'))
print(string_info ('Cats and dogs' ))
print(string_info ('DragoNS'))
print(is_contains('UrbaN', ['Кошка', 'Собака', 'urban']))
print(is_contains('Fruits', ['aPPle', 'OranGE', 'baNaNA']))
print('Количество функций: ', calls)
