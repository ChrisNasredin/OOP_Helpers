import random

fretboard = [
    ['F', 'F#', 'G', 'G#', 'A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E'],
    ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B'],
    ['G#', 'A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G'],
    ['D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B', 'C', 'C#', 'D'],
    ['A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A'],
    ['F', 'F#', 'G', 'G#', 'A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E']
]
empty_fretboard = [[''for i in range(12)]for i in range(6)]

# for string in fretboard:
#     print('|', end='')
#     for note in string:
#         print(note.center(4, '-'), end='|')
#     print()
# print(' ', end='')
# for dot in ['.', '', '.', '', '.', '', '.', '', '.', '', '', ':']:
#     print(dot.center(4), end=' ')
# print()
while True:
    quest = (random.randint(0, 5), random.randint(0, 11))
    empty_fretboard[quest[0]][quest[1]] = '?'
    for string in empty_fretboard:
        print('|', end='')
        for note in string:
            print(note.center(4, '-'), end='|')
        print()
    print(' ', end='')
    for dot in ['.', '', '.', '', '.', '', '.', '', '.', '', '', ':']:
        print(dot.center(4), end=' ')
    print()
    answer = input('Input Note: ')
    if answer == fretboard[quest[0]][quest[1]]:
        print('Bingo!')
    else:
        print('Nope')
    empty_fretboard[quest[0]][quest[1]] = '-'