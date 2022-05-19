


numbers = input('Введите любые цифры через ",", "/" или ";": ')
numbers.replace(',', ' ').replace(';', ' ').replace('/', ' ').split()
numbers_list = set(numbers)
numbers_list.discard(',')
numbers_list.discard('/')
numbers_list.discard(';')
print('Результат:', ','.join(numbers_list))


