# Задача №8
# Выявление цифры 5 в числе
answers = input('Введите число: ')
list_answers = list(answers)
if list_answers.count('5') == 0:
    print('В данном числе нет цифры 5')
else:
    print('В данном числе есть цифра 5')