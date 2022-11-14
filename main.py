lst = "а,б,в,г,д,е,ё,ж,з,и,й,к,л,м,н,о,п,р,с,т,у,ф,х,ц,ч,ш,щ,ъ,ы,ь,э,ю,я".split(",")  # Создаем список из всех русских букв
dct = {i: lst.index(i) + 1 for i in lst}  # Создаём словарь, который приравнивает букву к её номеру в русском алфавите


def check(var, var2, index=0):  # Функция для проверки, того какая буква идёт первее в алфавите

    if dct[var[index]] < dct[var2[index]]:   # Возращает True, если var идёт раньше в алфавите чем var2
        return True

    if dct[var[index]] == dct[var2[index]]:  # Если буквы равны
        return check(var, var2, index + 1)  # То проверяем следующую букву в слове

    return False  # Возращаем False, если прошлые проверки не удались


def alphabet_sort(list):  # Функция сортировки списка
    if len(list) < 2:  # <-- Базовый случай - Если в списке остался 1 или менее элементов, то завершаем рекурсию и возращаем список
        return list
    else:
        base = random.choice(list)  # Выбираем случайный элемент в списке в качестве опорного
        list.remove(base)  # И удаляем этот элемент из списка, чтобы не было повтора
        less = [i for i in list if check(i.lower(), base.lower())]  # Записываем в список, все значения которые идут раньше опорного
        greater = [i for i in list if check(base.lower(), i.lower())]  # Записываем в список, все значения которые идут позже опорного
        return alphabet_sort(less) + [base] + alphabet_sort(greater)  # Создаём рекурсию для дальнейшей проверки и суммируем всё
