class Matrix:
    def __init__(self, col, row=None, *, fill='0'):
        self._col = col
        self._row = row if row is not None else col
        self.MatrixList = [[fill for i in range(self._row)] for i in range(self._row)]
    def __repr__(self):
        repr = ''
        for row in self.MatrixList:
            repr += ('| ' + ' | '.join(row) + ' |\n' )
        return repr
A = Matrix(6, 10, fill='-')
print(A)
