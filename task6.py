# Задача №6
# Сумма цифр числа
numbers = input('Введите число: ')
list_numbers = list(numbers)
my_sum = 0
for number in list_numbers:
    number = int(number)
    my_sum += number

print('Сумма цифр числа',numbers,'равна',my_sum)



