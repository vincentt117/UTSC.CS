class Matrix():
    ''' A class which represents a mathematical matrix
    '''

    def __init__(self, content):
        '''(Matrix, list of obj) -> None
        Creates a matrix where a dictionary with keys as two element lists
        containing the row (element zero) and column (element one) position
        of the object (stored as value). For example: {[1, 7]: 43}, 43
        would be the object in the 1st row 7th column in the matrix.
        The values passed into init in the form of a list of objects.
        The list of integers, dimension, will dictate the dimensions of the
        matrix. Dimension exist in the form of [n, m] where n and m are positve
        integers that can be equal to one anther. The method will take n
        objects from content and form the first column, it will continue to
        do this until there are m columns.
        REQ: content must contain elements such that the matrix is a valid
        matrix; there are an appropriate number of elements given the number
        of rows and columns.
        '''
        pass

    def add_sub(self, target, add_or_sub):
        '''(Matrix, Matrix, bool) -> None
        Given another Matrix, perform either matrix addition or subtraction
        based on the value of add_or_sub. If add_or_sub is True perform
        addition, else (it being False) perform subtraction.
        REQ: Elements which reside in the same coordinate of either matrices
        must be of the same object type and must be able to added/subtracted
        from one another by some context
        '''
        pass

    def transpose(self):
        '''(Matrix) -> None
        Perform a matrix tranposition on the matrix calling the method. The
        operation will invert the coordinates of all objects contained in the
        matrix: row values become column values and vice versa
        '''
        pass

    def multi(self, target):
        '''(Matrix, Matrix) -> None
        Given another Matrix, perform matrix multiplication with the calling
        matrix on the left hand side of the operation and the target matrix
        on the right. Method will perform multiplication as described by
        standard matrix operation.
        REQ: number of column of the calling matrix must be equal to the number
        of rows of the targe matrix
        REQ: All elements within the calling matrix and the matrix being called
        must be integers or floats
        '''
        pass

    def switch(self, row_or_col, switched):
        '''(Matrix, bool, list of ints) -> None
        Switch two columns or two rows of a calling matrix. If row_or_col is
        True, switch the two rows contained in switched. For example, if
        row_or_col is True and switched is [1,3] switch the first and third
        rows of the matrix. If row_or_col is False, perform the same action,
        but switch columns instead.
        REQ: Matrix must possess the rows or columns contained in switch
        REQ: switched contains exactly two integers
        '''
        pass

    def get_by_row_or_col(self, coordinate, row_or_col):
        '''(Matrix, list of ints) -> obj
        Return a particular object in the matrix by a certain column or row
        and a position in the row or column. row_or_col dictates whether or not
        the object is referenced by row or column. If row_or_col is True, it is
        referencing by row, else it is referencing by row. Coordinate contains
        two integers, where the first is the coordinate[0]-th row or column and
        the second is the coordinate[1]-th item in that row/column
        For example if coordinate is [3, 4], and
        row_or_col is True return the 4th item in the third column.
        REQ: Designate coordinate must exist within the matrix
        '''
        pass

    def set_by_row_or_col(self, replace, coordinate, row_or_col):
        '''(Matrix, obj, list of ints, bool) -> None
        Replace a particular object in the matrix by a certain column or row
        and a position in the row or column. row_or_col dictates whether or not
        the object is referenced by row or column. If row_or_col is True, it is
        referencing by row, else it is referencing by row. Coordinate contains
        two integers, where the first is the coordinate[0]-th row or column and
        the second is the coordinate[1]-th item in that row/column
        For example if coordinate is [3, 4], and
        row_or_col is True return the 4th item in the third column.
        REQ: Designate coordinate must exist within the matrix
        REQ: Cannot be called upon by symmetric or identity matrix in a way
        that would compromise their property of being symmetric or an identity
        '''
        pass

    def get_determinant(self):
        '''(Matrix) -> int
        Returns the determinant of the matrix. The determinant being the
        difference of the product of the item in the first row first column
        and item in the second row second column and the product of the item in
        the first row second column and the second row first column.
        REQ: Matrix must be 2 by 2 and contain only ints
        '''
        pass

    def set_content(self, content):
        '''(Matrix, list of obj) -> None
        Sets the content of a given Matrix; replacing all elements.
        REQ: content must be appropriate to dimensions of calling matrix
        '''
        pass


class SquareMatrix(Matrix):
    '''A class which represents a n by n matrix
    '''

    def get_by_daig(self, duel_coor):
        ''' (Matrix, int) -> obj
        Return the object at a diagonal position in the calling matrix. For
        example, if duel_coor is 6, return the item at the 6th column in
        the 6th row.
        REQ: Matrix must contain at least as many diagonals as illustraded by
        duel_coor
        '''
        pass

    def set_by_diag(self, replace, duel_coor):
        ''' (Matrix, obj, int) -> None
        Replace the object at the diagonal specified by duel_coor with
        the object replace.For example, if duel_coor is 6, replace the item
        at the 6th column in the 6th row.
        REQ: Matrix must contain at least as many diagonals as illustraded by
        duel_coor
        '''
        pass


class SymmetricMatrix(SquareMatrix):
    '''A class which represents a n by n symmetrix matrix
    '''

    def set_by_row_or_col(self, replace, coordinate, treat_as_sym):
        '''(Matrix, obj, list of ints, bool, bool) -> None
        Replace a particular object in the matrix by a certain column or row
        and a position in the row or column. row_or_col dictates whether or not
        the object is referenced by row or column. If row_or_col is True, it is
        referencing by row, else it is referencing by row. Coordinate contains
        two integers, where the first is the coordinate[0]-th row or column and
        the second is the coordinate[1]-th item in that row/column
        For example if coordinate is [3, 4], and
        row_or_col is True return the 4th item in the third column.
        REQ: Designate coordinate must exist within the matrix
        '''
        pass


class IdentityMatrix(SymmetricMatrix):
    ''' A class which represents an identity matrix
    '''

    def __init__(self, value=1, dimension):
        ''' (Matrix, obj, int) -> None
        Create an indentity matrix with the object 'value' populating the
        diaglonal of the matrix and square dimensions as illustrated by
        dimension. By difault, the diagonals will be populated with integer 1.
        '''
        pass


class OneDMatrix(Matrix):
    ''' A class which represents a one dimentional matrix
    '''

    def get_val(self, target_val):
        ''' (Matrix, int) -> obj
        Return the object held in the target_val-th position of the matrix.
        REQ: Matrix must have as many positions as illustrated by target_val
        '''
        pass

    def set_val(self, target_val, replace):
        ''' (Matrix, int, obj) -> None
        Replace the object at the target_val-th position of the matrix with
        the replace value.
        REQ: Matrix must have as many positions as illustrated by target_val
        '''
        pass
