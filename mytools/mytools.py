def representationDict(dct, deep=0):
    '''
    Рекурсивная функция для более удобного представления словаря - показывает вложенные словари с отступами.
    Ну и заодно учит меня работать с рекурсивными функциями.
    '''
    if not isinstance(dct, dict):
        return f"'{dct}'," if isinstance(dct, str) else f"{dct},"
    deep += 1
    tabs = '\t' * deep
    lastoct = '},' if deep > 1 else '}'
    return '{\n' + '\n'.join(
        [f"{tabs} '{k}': {representationDict(v, deep)}" for k, v in dct.items()]) + '\n' + tabs[:-1] + lastoct


def representationList(lst, deep=0):
    '''
        Рекурсивная функция для более удобного представления списков - показывает вложенные списки с отступами.
        Ну и заодно учит меня работать с рекурсивными функциями.
    '''
    if not all(map(lambda x: isinstance(x, list), lst)):
        return lst
    deep += 1
    tabs = '\t' * deep
    lastoct = ']' if deep > 1 else ']'
    return '[\n' + '\n'.join([f'{tabs}{representationList(i, deep)},' for i in lst]) + '\n' + tabs[:-1] + lastoct


def deepsearch(sequence, request, index=''):
    '''
        Функция, которая ищет первое вхождение во вложенных структурах и отдает их в виде индексов.
        Я не знаю, зачем она может пригодиться, я просто захотел ее написать и написал, потому что смог.
    '''
    results = []
    print(locals())
    for i in range(len(sequence)):
        if sequence[i] == request:
            index += f'[{i}]'
            return index
        if isinstance(sequence[i], list):
            index += f'[{i}]'
            return deepsearch(sequence[i], request, index=index)
