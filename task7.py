# Задача №7
# Произведение цифр числа
numbers = input('Введите число: ')
list_numbers = list(numbers)
my_sum = 1
for number in list_numbers:
    number = int(number)
    my_sum *= number

print('Произведение цифр числа',numbers,'равно',my_sum)