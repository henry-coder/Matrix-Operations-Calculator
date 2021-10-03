import numpy as np
from scipy import sparse
from PrintStyles import PrintStyles as ps

def read_matrix(name: str = ''):
    values = []
    i = int(input(f'{ps.VIOLET}Enter the {ps.ITALIC}number of rows{ps.RESET+ps.VIOLET} of the matrix {ps.BVIOLET}{name}{ps.RESET}: '))
    print(f'{ps.YELLOW}Enter column values {ps.BOLD}separated by spaces{ps.RESET+ps.YELLOW}!')
    for line in range(1, i+1):
        line = input(f'{ps.BLUE}{line}ª line:{ps.RESET} ').split(' ')
        row = []
        for num in line:
            row.append(float(num))
        values.append(row)
    return Matrix(values)


class Matrix():
    def __init__(self, values):
        '''Initializes an object of type Matrix.
        ---
        Parameters:
        - values: a list of list (Matrix values)
        ---
        Returns:
        - Matrix object'''
        self.values = np.array(values)

    def __valid_operands(self, other):
        '''Internal function to validate operands'''
        if not(isinstance(other, Matrix) or isinstance(other, int) or isinstance(other, float)):
            raise TypeError(f'it is not possible to perform the operation between a Matrix and the {type(other)}')
        return other.values if isinstance(other, Matrix) else other

    @property
    def dimension(self):
        '''Returns a tuple with the dimensions of the matrix.
        ---
        Returns:
        - tuple(number of rows,number of columns) '''
        return self.values.shape

    @property
    def determinant(self):
        '''Returns the matrix determinant.
        *the determinant is rounded to a int number'''
        return int(np.linalg.det(self.values))

    @property
    def sparsity(self):
        '''Returns the sparsity of the matrix.'''
        return 1 - np.count_nonzero(self.values)/self.values.size

    @property
    def is_line(self):
        '''Returns true if the matrix is a line matrix and false otherwise.'''
        return self.dimension[0] == 1

    @property
    def is_column(self):
        '''Returns true if the matrix is a column matrix and false otherwise.'''
        return self.dimension[1] == 1

    @property
    def is_square(self):
        '''Returns true if the matrix is a square matrix and false otherwise.'''
        return self.dimension[0] == self.dimension[1]

    @property
    def is_null(self):
        '''Returns true if the matrix is a null matrix and false otherwise.'''
        return np.count_nonzero == 0

    @property
    def is_identity(self):
        '''Returns true if the matrix is a indentity matrix and false otherwise.'''
        return self == Matrix(np.identity(self.dimension[0], int))

    @property
    def is_symmetric(self):
        '''Returns true if the matrix is a symmetric matrix and false otherwise.'''
        return self.is_square and self == self.transpose

    @property
    def is_antisymmetric(self):
        '''Returns true if the matrix is a antisymmetric matrix and false otherwise.'''
        if not self.is_square:
            return False
        return -self == ~self

    @property
    def is_orthogonal(self):
        '''Returns true if the matrix is a orthogonal matrix and false otherwise.'''
        if not self.is_square:
            return False
        return ~self == self.transpose

    @property
    def characteristics(self):
        '''Get the matrix characteristics'''
        values = (self.is_line, self.is_column, self.is_null, self.is_square, self.is_identity, self.is_symmetric, self.is_antisymmetric, self.is_orthogonal)
        keys = ('line', 'column', 'null', 'square', 'identity', 'symmetrical', 'antisymmetrical', 'orthogonal')
        return dict(zip(keys, values))

    @property
    def sparse(self):
        '''Returns the matrix in a sparse matrix representation.'''
        return sparse.csr_matrix(self.values)

    @property
    def lower_triangular(self):
        '''Returns the lower triangular matrix'''
        return Matrix(np.tril(self.values))

    @property
    def upper_triangular(self):
        '''Returns the upper triangular matrix'''
        return Matrix(np.triu(self.values))

    @property
    def transpose(self):
        '''Returns the transposed matrix'''
        return Matrix(self.values.transpose())

    @property
    def diagonal(self):
        '''Returns the diagonal matrix'''
        return Matrix([np.diag(self.values)])

    def __invert__(self):
        '''Returns the inverse matrix.
        ---
        Syntax: ~Matrix'''
        return Matrix(np.linalg.inv(self.values))

    def __neg__(self):
        '''Returns the opposite matrix.
        ---
        Syntax: -Matrix'''
        return self - self - self

    def __add__(self, other):
        '''Returns the result of the addition operation with the matrix.
        ---
        Syntax:
        - Matrix + Matrix
        - Matrix + int
        - Matrix + float
        - int + Matrix
        - float + Matrix'''
        other = self.__valid_operands(other)
        return Matrix(self.values + other)

    def __sub__(self, other):
        '''Returns the result of the subtraction operation with the matrix.
        ---
        Syntax:
        - Matrix - Matrix
        - Matrix - int
        - Matrix - float
        - int - Matrix
        - float - Matrix'''
        other = self.__valid_operands(other)
        return Matrix(self.values - other)

    def __mul__(self, other):
        '''Returns the result of the multiplication operation with the matrix and a scalar number.
        ---
        Syntax:
        - Matrix * int
        - Matrix * float
        - int * Matrix
        - float * Matrix'''
        other = self.__valid_operands(other)
        return Matrix(self.values * other)

    def __matmul__(self, other):
        '''Returns the result of the multiplication operation with the matrix and a scalar number.
        ---
        Syntax:
        - Matrix * Matrix'''
        other = self.__valid_operands(other)
        return Matrix(self.values @ other)

    def __str__(self):
        '''Returns the string representation of this Matrix object'''
        txt = f'{ps.BCYAN}'
        for line in self.values:
            txt += f'|{ps.RESET}{ps.BLUE}'
            for value in line:
                txt += f'{value:5.2f} '
            txt += f'{ps.BCYAN}|\n'
        dimension = self.dimension
        txt += f'{ps.IGREEN}{dimension[0]} X {dimension[1]}{ps.RESET}'
        return txt.replace(',', '').replace('.', ',').replace(',00', '')

    def __eq__(self, other):
        '''method responsible for defining equality between matrices.'''
        if isinstance(other, Matrix):
            return (self.values == other.values).all()
        return False
