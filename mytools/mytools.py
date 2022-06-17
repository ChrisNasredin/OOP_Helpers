def representationDict(dct, deep=0):
    if not isinstance(dct, dict):
        return f"'{dct}'," if isinstance(dct, str) else f"{dct},"
    deep += 1
    tabs = '\t' * deep
    lastoct = '},' if deep > 1 else '}'
    return '{\n' + '\n'.join(
        [f"{tabs} '{k}': {representationDict(v, deep)}" for k, v in dct.items()]) + '\n' + tabs[:-1] + lastoct


def representationList(lst, deep=0):
    if not all(map(lambda x: isinstance(x, list), lst)):
        return lst
    deep += 1
    tabs = '\t' * deep
    lastoct = ']' if deep > 1 else ']'
    return '[\n' + '\n'.join([f'{tabs}{representationList(i, deep)},' for i in lst]) + '\n' + tabs[:-1] + lastoct


def deepsearch(sequence, request, index=''):
    results = []
    print(locals())
    for i in range(len(sequence)):
        if sequence[i] == request:
            index += f'[{i}]'
            return index
        if isinstance(sequence[i], list):
            index += f'[{i}]'
            return deepsearch(sequence[i], request, index=index)
