
number_of_elements = int(input('Введите количество элементов: '))
elements = []

for i in range(number_of_elements):
    i += 1
    element = input(f'Введите {i} элемент: ')
    elements.append(element)

elements.sort()
print('Вывод:', elements)











