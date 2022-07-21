import random


class Fretboard:
    FRETBOARD = [
        ['F', 'F#', 'G', 'G#', 'A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E'],
        ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B'],
        ['G#', 'A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G'],
        ['D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B', 'C', 'C#', 'D'],
        ['A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A'],
        ['F', 'F#', 'G', 'G#', 'A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E']
    ]
    EMPTY_FRETBOARD = [['' for i in range(12)] for i in range(6)]
    REPEAT_DCT = {}

    @staticmethod
    def RandomNote(strings=5, frets=11):
        if Fretboard.REPEAT_DCT:
            if random.randint(0,1):
                return (random.randint(0, strings), random.randint(0, frets))
            else:
                return random.choices(list(Fretboard.REPEAT_DCT.keys()))[0]
        else:
            return (random.randint(0, strings), random.randint(0, frets))
    @staticmethod
    def show_fretboard(fretboard):
        result = ''
        for string in fretboard:
            result += '|'
            for note in string:
                result += note.center(4, '-') + '|'
            result += '\n'
        result += ' '
        for dot in ['.', '', '.', '', '.', '', '.', '', '.', '', '', ':']:
            result += dot.center(4, ' ') + ' '
        result += '\n'
        return result

    @classmethod
    def change_repeat_dct(cls, action, note_coord):
        if action == 'add':
            if note_coord not in cls.REPEAT_DCT:
                cls.REPEAT_DCT[note_coord] = 1
            else:
                cls.REPEAT_DCT[note_coord] += 1
        elif action == 'delete':
            if note_coord in cls.REPEAT_DCT:
                if cls.REPEAT_DCT[note_coord] == 1:
                    del cls.REPEAT_DCT[note_coord]
                else:
                    cls.REPEAT_DCT[note_coord] -= 1

    def question(self):
        ans_note = self.__class__.RandomNote()
        #print(ans_note)
        self.__class__.EMPTY_FRETBOARD[ans_note[0]][ans_note[1]] = '?'
        print(self.__class__.show_fretboard(self.__class__.EMPTY_FRETBOARD))
        Answer = input('Input Note ')
        if Answer == self.__class__.FRETBOARD[ans_note[0]][ans_note[1]]:
            print('Bingo!')
            self.change_repeat_dct('delete', ans_note)
        else:
            print('Nope')
            self.change_repeat_dct('add', ans_note)
        self.__class__.EMPTY_FRETBOARD[ans_note[0]][ans_note[1]] = '-'


MyTest = Fretboard()
while True:
    MyTest.question()
    print(MyTest.REPEAT_DCT)

