# Методы list
# append(х) - Добавляет элемент в конец списка.
# remove(x) - Удаляет первый элемент в списке, имеющий значение x. ValueError, если такого элемента не существует.
# count(x) - 	Возвращает количество элементов со значением x.
# sort([key=функция]) - Сортирует список на основе функции.
# insert(i, x) - Вставляет на i-ый элемент значение x.


# Методы dict
# get(key[, default]) - возвращает значение ключа, но если его нет, не бросает исключение, а возвращает default
#                       (по умолчанию None).
# items() - возвращает пары (ключ, значение).
# keys() - возвращает ключи в словаре.
# values() - возвращает значения в словаре.
# fromkeys(seq[, value]) - создает словарь с ключами из seq и значением value (по умолчанию None).


# Методы str
# len(S) - Длина строки.
# split(символ) - Разбиение строки по разделителю.
# title() - Первую букву каждого слова переводит в верхний регистр, а все остальные в нижний.
# lower() - Преобразование строки к нижнему регистру.
# upper() - Преобразование строки к верхнему регистру.


# Методы set
# add(elem) - добавляет элемент в множество.
# discard(elem) - удаляет элемент, если он находится в множестве.
# difference_update(other, ...); set -= other | ... - вычитание.
# update(other, ...); set |= other | ... - объединение.
# set == other - все элементы set принадлежат other, все элементы other принадлежат set.