# Задача №10
# Количество цифр 5 в числе
number = input('Введите число: ')
list_number = list(number)
if list_number.count('5') == 0:
    print('В данном числе отсутствует цифра 5')
else:
    print('В данном числе', (list_number.count('5')), '5-ка(ки)')