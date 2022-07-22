#! /usr/bin/env python3
import random


class Fretboard:
    def __init__(self, exam=False):
        self.FRETBOARD = [
            ['F', 'F#', 'G', 'G#', 'A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E'],
            ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B'],
            ['G#', 'A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G'],
            ['D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B', 'C', 'C#', 'D'],
            ['A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A'],
            ['F', 'F#', 'G', 'G#', 'A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E']
        ]
        self.EMPTY_FRETBOARD = [['' for i in range(12)] for i in range(6)]
        self.REPEAT_DCT = {}
        self.EXAM_DCT = {}
        self.exam = exam

    def RandomNote(self, strings=5, frets=11):
        if self.exam:
            print('Exam', self.EXAM_DCT)
            exam_note = (random.randint(0, strings), random.randint(0, frets))
            while exam_note in self.EXAM_DCT:
                exam_note = (random.randint(0, strings), random.randint(0, frets))
            return exam_note
        else:
            if self.REPEAT_DCT:
                if random.randint(0, 1):
                    return (random.randint(0, strings), random.randint(0, frets))
                else:
                    return random.choices(list(self.REPEAT_DCT.keys()))[0]
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

    def change_repeat_dct(self, action, note_coord):
        if action == 'add':
            if note_coord not in self.REPEAT_DCT:
                self.REPEAT_DCT[note_coord] = 1
            else:
                self.REPEAT_DCT[note_coord] += 1
        elif action == 'delete':
            if note_coord in self.REPEAT_DCT:
                if self.REPEAT_DCT[note_coord] == 1:
                    del self.REPEAT_DCT[note_coord]
                else:
                    self.REPEAT_DCT[note_coord] -= 1

    def question(self):
        if self.exam:
            if len(self.EXAM_DCT) >= 72:
                print('Mistakes: ', sum([1 for k, v in self.EXAM_DCT.items() if not v]))
                return
        ans_note = self.RandomNote()
        self.EMPTY_FRETBOARD[ans_note[0]][ans_note[1]] = '?'
        print(self.__class__.show_fretboard(self.EMPTY_FRETBOARD))
        Answer = input('Input Note ')
        if Answer == self.FRETBOARD[ans_note[0]][ans_note[1]]:
            print('Bingo!')
            if self.exam:
                self.EXAM_DCT[ans_note] = True
            else:
                self.change_repeat_dct('delete', ans_note)
        else:
            print('Nope')
            if self.exam:
                self.EXAM_DCT[ans_note] = False
            else:
                self.change_repeat_dct('add', ans_note)
        self.EMPTY_FRETBOARD[ans_note[0]][ans_note[1]] = '-'
    def start_game(self):
        if self.exam:
            for _ in range(73):
                self.question()
        else:
            while True:
                self.question()


MyTest = Fretboard(exam=True)
MyTest.start_game()
