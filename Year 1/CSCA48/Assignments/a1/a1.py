class MatrixIndexError(Exception):
    '''An attempt has been made to access an invalid index in this matrix'''


class MatrixDimensionError(Exception):
    '''An attempt has been made to perform an operation on this matrix which
    is not valid given its dimensions'''


class MatrixInvalidOperationError(Exception):
    '''An attempt was made to perform an operation on this matrix which is
    not valid given its type'''


class MatrixNode():
    '''A general node class for a matrix'''

    def __init__(self, contents, right=None, down=None, i=None, j=None):
        '''(MatrixNode, obj, MatrixNode, MatrixNode, int, int) -> NoneType
        Create a new node holding contents, that is linked to right
        and down in a matrix and holds coordinates of i and j.
        '''
        self._contents = contents
        self._right = right
        self._down = down
        # Store the coordinate of the MatrixNode, if one is provided
        self._i = i
        self._j = j

    def __str__(self):
        '''(MatrixNode) -> str
        Return the string representation of this node
        '''
        return str(self._contents)

    def get_self(self):
        '''(MatrixNode) -> MatrixNode
        Returns the matrix node
        '''
        return self

    def get_contents(self):
        '''(MatrixNode) -> obj
        Return the contents of this node
        '''
        return self._contents

    def set_contents(self, new_contents):
        '''(MatrixNode, obj) -> NoneType
        Set the contents of this node to new_contents
        '''
        self._contents = new_contents

    def get_right(self):
        '''(MatrixNode) -> MatrixNode
        Return the node to the right of this one
        '''
        return self._right

    def set_right(self, new_node):
        '''(MatrixNode, MatrixNode) -> NoneType
        Set the new_node to be to the right of this one in the matrix
        '''
        self._right = new_node

    def get_down(self):
        '''(MatrixNode) -> MatrixNode
        Return the node below this one
        '''
        return self._down

    def set_down(self, new_node):
        '''(MatrixNode, MatrixNode) -> NoneType
        Set new_node to be below this one in the matrix
        '''
        self._down = new_node

    def get_i(self):
        '''(MatrixNode) -> NoneType
        Return the i cooridnate of the node
        '''
        return self._i

    def get_j(self):
        '''(MatrixNode) -> NoneType
        Return the j coordinate of the node
        '''
        return self._j


class Matrix():
    '''A class to represent a mathematical matrix'''

    def __init__(self, m, n, default=0):
        '''(Matrix, int, int, float) -> NoneType
        Create a new m x n matrix with all values set to default
        REQ: m and n must be 0 or positive
        '''
        if n < 0 or m < 0:
            raise MatrixDimensionError
        self._head = MatrixNode(None)
        # Store verticle and horizontal dimensions
        self._v_dim = m
        self._h_dim = n
        # Populate the matrix in the event here default is non-zero
        if default != 0:
            # Form index nodes for vertical component of the matrix
            cur_v = self._head
            for i in range(0, m):
                cur_v.set_down(MatrixNode(i))
                cur_v = cur_v.get_down()
            # Form index nodes for horizontal component of the matrix
            cur_h = self._head
            for j in range(0, n):
                cur_h.set_right(MatrixNode(j))
                cur_h = cur_h.get_right()
            # Form the content nodes
            for i in range(0, m):
                for j in range(0, n):
                    self.set_val(i, j, default)

    def __str__(self):
        '''(Matrix) -> str
        Return the string representation of this node
        '''
        ret_str = ''
        for y in range(0, self._v_dim):
            for x in range(0, self._h_dim):
                ret_str += str(self.get_val(y, x))
            ret_str += "\n"
        return ret_str

    def get_val(self, i, j):
        '''(Matrix, int, int) -> float
        Return the value of m[i,j] for this matrix m
        REQ: i and j must be within the dimensions of the calling matrix
        '''
        # If i or j exceed the dimensions of the matrix, hence an attempt to
        # access a value beyond exists in the matrix, MatrixDimensionError
        # is raised
        if i > self.get_v_dim() or j > self.get_h_dim() or i < 0 or j < 0:
            raise MatrixIndexError
        # Traverse through vertical index node to find the i'th index nod
        cur = self._head
        ind_not_found = True
        while ind_not_found:
            # Once the proper index is found, traverse right for the desired
            # content node
            cur = cur.get_down()
            if not cur or cur.get_contents() > i:
                        content = 0
                        ind_not_found = False
            elif cur.get_contents() == i:
                while ind_not_found:
                    cur = cur.get_right()
                    if not cur or cur.get_j() > j:
                        content = 0
                        ind_not_found = False
                    elif cur.get_j() == j:
                        content = cur.get_contents()
                        ind_not_found = False
        return content

    def set_val(self, i, j, new_val):
        '''(Matrix, int, int, float) -> NoneType
        Set the value of m[i,j] to new_val for this matrix m
        REQ: i and j must be within the dimensions of the calling matrix
        '''
        # If i or j exceed the dimensions of the matrix, hence an attempt to
        # access a value beyond exists in the matrix, MatrixDimensionError
        # is raised
        if i >= self.get_v_dim() or j >= self.get_h_dim() or i < 0 or j < 0:
            raise MatrixIndexError

        # Case 1: Content at m[i, j] is not 0 and new_val is not 0
        if self.get_val(i, j) != 0 and new_val != 0:
            self.set_val_nz_nz(i, j, new_val)

        # Case 2: Content at m[i, j] is not 0 and new_val is zero
        elif self.get_val(i, j) != 0 and new_val == 0:
            self.set_val_nz_z(i, j, new_val)

        # Case 3: Content at m[i, j] is zero and new_val is not zero
        elif self.get_val(i, j) == 0 and new_val != 0:
            self.set_val_z_nz(i, j, new_val)

        # Case 4: Content at m[i, j] is zero and new_val is zero
        # In this case, nothin needs to be done as nothing changes

    def set_val_nz_nz(self, i, j, new_val):
        '''(Matrix, int, int, float) -> NoneType
        Set the value of m[i, j] to new_val for this matrix m in the event
        where new_val is zero and the previous value at m[i, j] is not zero
        REQ: i and j must be within the dimensions of the calling matrix
        REQ: new_val and m[i, j] must both not be zero
        '''
        # Traverse the vertical index nodes to find node at i
        cur = self._head
        while cur.get_contents() != i:
            cur = cur.get_down()
        # Once the desired node is found, traverse horizontally for
        # for the desired node and replace its content
        not_found = True
        while not_found:
            if cur:
                cur = cur.get_right()
            if cur.get_j() == j:
                not_found = False
        cur.set_contents(new_val)

    def set_val_nz_z(self, i, j, new_val):
        '''(Matrix, int, int, float) -> NoneType
        Set the value of m[i, j] to new_val for this matrix m in the event
        where new_val is zero and the previous value at m[i, j] is not
        zero
        REQ: i and j must be within the dimensions of the calling matrix
        REQ: m[i, j] must be not be zero
        REQ: new_val must be zero
        '''
        # Traverse the vertical index nodes to find node at i
        cur_v_h = self._head
        while cur_v_h.get_contents() != i:
            pre_v_h = cur_v_h
            cur_v_h = cur_v_h.get_down()
        while cur_v_h.get_j() != j:
            pre_v_h = cur_v_h
            cur_v_h = cur_v_h.get_right()
        # Traverse the horizontal index nodes to find node at j
        cur_h_v = self._head
        while cur_h_v.get_contents() != j:
            pre_h_v = cur_h_v
            cur_h_v = cur_h_v.get_right()
        while cur_h_v.get_i() != i:
            pre_h_v = cur_h_v
            cur_h_v = cur_h_v.get_down()
        # 'Remove' the node so as to illustrate the content at the
        # coordinate is 0, set the link of the removed link to none
        new_right = cur_v_h.get_right()
        pre_v_h.set_right(new_right)
        new_down = cur_h_v.get_down()
        pre_h_v.set_down(new_down)

    def set_val_z_nz(self, i, j, new_val):
        '''
        Set the value of m[i, j] to new_val for this matrix m in the event
        where new_val is not zero and the previous value at m[i, j] is zero
        REQ: i and j must be within the dimensions of the calling matrix
        REQ: m[i, j] must be not be zero
        REQ: new_val must be zero
        '''
        # Traverse the vertical and horizontal index to find the index
        # node corresponding to i and j, if those cannot be found create
        # them and linked them to their respective index lists
        cur_v_h = self._head
        vert_not_found = True
        while vert_not_found:
            pre_v_h = cur_v_h
            cur_v_h = cur_v_h.get_down()
            # Pointing at None (overshot)
            if not cur_v_h or cur_v_h.get_contents() > i:
                pre_v_h.set_down(MatrixNode(i))
                start_v_h = pre_v_h.get_down()
                start_v_h.set_down(cur_v_h)
                vert_not_found = False
            # Found desired index
            elif cur_v_h.get_contents() == i:
                start_v_h = cur_v_h
                vert_not_found = False
        # Traverse the horizontal content starting at vertical index i
        # for find the two content nodes prior and after the node at i j
        vert_h_cont_not_found = True
        while vert_h_cont_not_found:
            pre_start_v_h = start_v_h
            start_v_h = start_v_h.get_right()
            if not start_v_h or start_v_h.get_j() > j:
                vert_h_cont_not_found = False
        cur_h_v = self._head
        hori_not_found = True
        while hori_not_found:
            pre_h_v = cur_h_v
            cur_h_v = cur_h_v.get_right()
            # Pointing at None (overshot)
            if not cur_h_v or cur_h_v.get_contents() > j:
                pre_h_v.set_right(MatrixNode(j))
                start_h_v = pre_h_v.get_right()
                start_h_v.set_right(cur_h_v)
                hori_not_found = False
            # Found desired index
            elif cur_h_v.get_contents() == j:
                start_h_v = cur_h_v
                hori_not_found = False
        # Traverse the horizontal content starting at vertical index j
        # for find the two content nodes prior and after the node at i j
        hori_v_cont_not_found = True
        while hori_v_cont_not_found:
            pre_start_h_v = start_h_v
            start_h_v = start_h_v.get_down()
            if not start_h_v or start_h_v.get_i() > i:
                hori_v_cont_not_found = False
        # Link all tracked components to the new node
        pre_start_v_h.set_right(MatrixNode(new_val, start_v_h,
                                           start_h_v, i, j))
        new_cont = pre_start_v_h.get_right()
        pre_start_h_v.set_down(new_cont)

    def get_row(self, row_num):
        '''(Matrix, int) -> OneDimensionalMatrix
        Return the row_num'th row of this matrix
        REQ: row_num must be an index of the calling matrix
        '''
        # If row_num is not a vertical index of the matrix, raise
        # MatrixIndexError
        if row_num >= self.get_v_dim() or row_num < 0:
            raise MatrixIndexError

        # Traverse through vertical index nodes, if the desired node cannot
        # be found it contains only zeros.
        cur = self._head
        not_found = True
        while not_found:
            cur = cur.get_down()
            # Desired node does not exist, it contains only zeros and as such
            # return a row of zeros
            if not cur or cur.get_contents() > row_num:
                ret_row = OneDimensionalMatrix(self.get_h_dim())
                not_found = False
            # Desired node does exist, iterate through the new matrix and
            # set each value as the corresponding value in the original
            # Matrix
            elif cur.get_contents() == row_num:
                ret_row = OneDimensionalMatrix(self.get_h_dim())
                not_found = False
                for x in range(0, self.get_h_dim()):
                    ret_row.set_item(x, self.get_val(row_num, x))
        return ret_row

    def set_row(self, row_num, new_row):
        '''(Matrix, int, OneDimensionalMatrix) -> NoneType
        Set the value of the row_num'th row of this matrix to those of new_row
        REQ: row_num must be a vertical index of the calling matrix
        REQ: new_row must have at least one dimension that is equivalent to
        the row length of the calling matrix
        '''
        # This method is not accessible via SymmetricMatrix objects,
        # DiagonalMatrix, nor IdentityMatrix objects
        if type(self) == DiagonalMatrix or type(self) == IdentityMatrix:
            raise MatrixInvalidOperationError

        # If row_num is not a vertical index of the matrix, raise
        # MatrixIndexError
        if row_num >= self.get_v_dim() or row_num < 0:
            raise MatrixIndexError

        # If the dimension of new_row is not equivalent to that of the column
        # length of the calling matrix, raise MatrixDimensionError
        if new_row.get_h_dim() != self.get_h_dim()\
           and new_row.get_v_dim() != self.get_h_dim():
            raise MatrixDimensionError

        # Determine whether new_row is a nx1 or 1xn matrix. And traverse
        # it accordingly to retrieve row values

        # If new_row is 1xn
        # Variable added to resolve pep8 issue
        new_row_v = new_row.get_v_dim()
        if new_row.get_h_dim() == self.get_h_dim() and new_row_v == 1:
            # Traverse through the content nodes of the parameter matrix and
            # set each corresponding value in the calling matrix to the content
            # of the former
            for x in range(0, self.get_h_dim()):
                self.set_val(row_num, x, new_row.get_val(0, x))
        # If new_row is a diagonal matrix
        else:
            for x in range(0, self.get_h_dim()):
                self.set_val(row_num, x, new_row.get_val(x, x))

    def get_col(self, col_num):
        '''(Matrix, int) -> OneDimensionalMatrix
        Return the col_num'th column of this matrix
        REQ: col_num must be a horizontal index of the calling matrix
        '''
        # If col_num is not a horizontal index of the matrix, raise
        # MatrixIndexError
        if col_num >= self.get_h_dim() or col_num < 0:
            raise MatrixIndexError
        # Traverse through horizontal index nodes, if the desired node cannot
        # be found it contains only zeros.
        cur = self._head
        not_found = True
        while not_found:
            cur = cur.get_right()
            if not cur or cur.get_contents() > col_num:
                ret_col = OneDimensionalMatrix(self.get_v_dim())
                not_found = False
            # Desired node does exist, iterate through the new matrix and
            # set each value as the corresponding value in the original
            # Matrix
            elif cur.get_contents() == col_num:
                ret_col = OneDimensionalMatrix(self.get_v_dim())
                not_found = False
                for y in range(self.get_v_dim()):
                    ret_col.set_item(y, self.get_val(y, col_num))
        return ret_col

    def set_col(self, col_num, new_col):
        '''(Matrix, int, OneDimensionalMatrix) -> NoneType
        Set the value of the col_num'th column of this matrix to those of
        new_row
        REQ: col_num must be a horizontal index of the calling matrix
        REQ: new_col must have at least one dimension that is equivalent to
        that of the column length of the calling matrix
        '''
        # This method is not accessible via SymmetricMatrix objects,
        # DiagonalMatrix, nor IdentityMatrix objects
        if type(self) == DiagonalMatrix or type(self) == IdentityMatrix:
            raise MatrixInvalidOperationError

        # If col_num is not a horizontal index of this matrix, raise
        # MatrixIndexErrir
        if col_num >= self.get_h_dim() or col_num < 0:
            raise MatrixIndexError

        # If new_col's row and column length are not that of the calling
        # matrix's row length, raise MatrixDimensionError
        if new_col.get_v_dim() != self.get_v_dim() and\
           new_col.get_h_dim() != self.get_v_dim():
            raise MatrixDimensionError()

        # Determine whether new_col is a nx1 or 1xn matrix. And traverse
        # it accordingly to retrieve col values

        # new_col is 1xn
        if new_col.get_h_dim() == self.get_v_dim() \
           and new_col.get_v_dim() == 1:
            # Traverse through the content nodes of the parameter matrix and
            # set each corresponding value in the calling matrix to the
            # content of the former
            for y in range(0, self.get_v_dim()):
                self.set_val(y, col_num, new_col.get_val(0, y))
        # new_col is a diagonal matrix
        else:
            for y in range(0, self.get_v_dim()):
                self.set_val(y, col_num, new_col.get_val(y, y))

    def swap_rows(self, i, j):
        '''(Matrix, int, int) -> NoneType
        Swap the values of rows i and j in this matrix
        REQ: i and j must be row indices of the calling matrix
        '''
        # This method is not accessible via SymmetricMatrix objects,
        # DiagonalMatrix, nor IdentityMatrix objects
        if type(self) == DiagonalMatrix or type(self) == IdentityMatrix:
            raise MatrixInvalidOperationError

        # If either i or j are not part of the vertical index of the calling
        # Matrix, raise MatrixIndexError
        if i >= self.get_v_dim() or j >= self.get_v_dim() or i < 0 or j < 0:
            raise MatrixIndexError
        # Extract rows from i and j then set them the location of the other
        new_j = self.get_row(i)
        new_i = self.get_row(j)
        self.set_row(j, new_j)
        self.set_row(i, new_i)

    def swap_cols(self, i, j):
        '''(Matrix, int, int) -> NoneType
        Swap the values of columns i and j in this matrix
        REQL i and j must be column indices of the calling matrix
        '''
        # This method is not accessible via SymmetricMatrix objects,
        # DiagonalMatrix, nor IdentityMatrix objects
        if type(self) == DiagonalMatrix or type(self) == IdentityMatrix:
            raise MatrixInvalidOperationError

        # If either i or j are not part of the horizontal index othe calling
        # Matrix, raise MatrixIndexError
        if i >= self.get_h_dim() or j >= self.get_h_dim() or i < 0 or j < 0:
            raise MatrixIndexError
        # Extract columns from i and j then set them the location of the other
        new_j = self.get_col(i)
        new_i = self.get_col(j)
        self.set_col(j, new_j)
        self.set_col(i, new_i)

    def add_scalar(self, add_value):
        '''(Matrix, float) -> NoneType
        Increase all values in this matrix by add_value
        '''
        # This method is not accessible via DiagonalMatrix, nor
        # IdentityMatrix objects
        if type(self) == DiagonalMatrix or type(self) == IdentityMatrix:
            raise MatrixInvalidOperationError

        # Iterate through all elements and set their values to what they were
        # increase by add_value
        for x in range(0, self.get_h_dim()):
            for y in range(0, self. get_v_dim()):
                self.set_val(y, x, self.get_val(y, x) + add_value)

    def subtract_scalar(self, sub_value):
        '''(Matrix, float) -> NoneType
        Decrease all values in this matrix by sub_value
        '''
        # This method is not accessible via DiagonalMatrix, nor
        # IdentityMatrix objects if the value is not zero
        if sub_value != 0 and\
           (type(self) == DiagonalMatrix or type(self) == IdentityMatrix):
            raise MatrixInvalidOperationError

        # Execute adds_scalar via a negative value
        self.add_scalar(-sub_value)

    def multiply_scalar(self, mult_value):
        '''(Matrix, float) -> NoneType
        Multiply all values in this matrix by mult_value
        '''
        # This method is not accessibe via Identity matrix if mult_value is not
        # 1
        if type(self) == IdentityMatrix and mult_value != 1:
            raise MatrixInvalidOperationError
        # Iterate through all elements and set their values to what they were
        # multiplied by by mult_value
        for x in range(0, self.get_h_dim()):
            for y in range(0, self. get_v_dim()):
                self.set_val(y, x, self.get_val(y, x) * mult_value)

    def add_matrix(self, adder_matrix):
        '''(Matrix, Matrix) -> Matrix
        Return a new matrix that is the sum of this matrix and adder_matrix
        REQ: The calling matrix and adder matrix must have identitcal
        dimensions
        '''
        # If the size of the matrices are difference, raise
        # MatrixDimensionError
        if self.get_v_dim() != adder_matrix.get_v_dim() or\
           self.get_h_dim() != adder_matrix.get_h_dim():
            raise MatrixDimensionError
        ret_mat = Matrix(self.get_v_dim(), self.get_h_dim())
        # Iterate through all elements of the calling matrix and increase
        # their values by the value in the corresponding element of
        # adder_matrix
        for x in range(0, self.get_h_dim()):
            for y in range(0, self. get_v_dim()):
                ret_mat.set_val(y, x, self.get_val(y, x) +
                                adder_matrix.get_val(y, x))
        return ret_mat

    def multiply_matrix(self, mult_matrix):
        '''(Matrix, Matrix) -> Matrix
        Return a new matrix that is the product of this matrix and mult_matrix
        REQ: Column length of the calling matrix must be equal to the row
        lenght of mult_matrix
        '''
        # If the column lenght of the calling matrix and the row length of
        # mult_matrix are different, raise MatrixDimensionError
        if self.get_h_dim() != mult_matrix.get_v_dim():
            raise MatrixDimensionError
        ret_mat = Matrix(self.get_v_dim(), mult_matrix.get_h_dim())
        # Iterate through i'th row of the calling matrix and the j'th column
        # of mult_matrix. Multiply each value and sum them, the result will
        # be the value of ret_mat[i, j]
        for j in range(0, ret_mat.get_h_dim()):
            for i in range(0, ret_mat.get_v_dim()):
                cur_cord = 0
                for n in range(0, self.get_h_dim()):
                    cur_cord += self.get_val(i, n) * mult_matrix.get_val(n, j)
                ret_mat.set_val(i, j, cur_cord)
        return ret_mat

    def get_v_dim(self):
        '''(Matrix) -> int
        Return the vertical dimension of the calling matrix
        '''
        return self._v_dim

    def get_h_dim(self):
        '''(Matrix) -> int
        Return the horizontal dimension of the calling matrix
        '''
        return self._h_dim

    def get_head(self):
        '''(Matrix) -> MatrixNode
        Return the Matrix Node representing the head of the calling of the
        calling matrix
        '''
        return self._head


class OneDimensionalMatrix(Matrix):
    '''A 1xn or nx1 matrix.
    (For the purposes of multiplication, we assume it's 1xn)'''
    def __init__(self, n, default=0):
        '''(OneDimensionalMatrix, int, int, float) -> NoneType
        Create a new 1xn or nx1 matrix with all values set to default
        '''
        # Always intialize a OneDimensionalMatrix as a row matrix (1xn)
        Matrix.__init__(self, 1, n, default)

    def get_item(self, i):
        '''(OneDimensionalMatrix, int) -> float
        Return the i'th item in this matrix
        REQ: i must be an index in the matrix
        '''
        # If i is not an index in the matrix, raise MatrixIndexError
        if i > self.get_h_dim() or i < 0:
            raise MatrixIndexError
        # In the even where the matrix is a diagonal matrix, return value
        # at i, i
        if self.get_h_dim() > 1 and self.get_v_dim() > 1:
            content = self.get_val(i, i)
        else:
            content = self.get_val(0, i)
        return content

    def set_item(self, i, new_val):
        '''(OneDimensionalMatrix, int, float) -> NoneType
        Set the i'th item in this matrix to new_val
        REQ: i must be an index in the matrix
        '''
        # This method is not accessible via IdentityMatrix object
        if type(self) == IdentityMatrix:
            raise MatrixInvalidOperationError
        # If i is nt an index of the matrix, raise MatrixIndexError
        if i > self.get_h_dim() or i < 0:
            raise MatrixIndexError
        # Retrieve item at 0, i if the matrix is 1xn
        if self.get_h_dim() == 1 or self.get_v_dim() == 1:
            self.set_val(0, i, new_val)
        else:
            self.set_val(i, i, new_val)

    def get_row(self, n=0):
        '''(OneDimensionalMatrix) -> OneDimensionalMatrix
        Return the calling matrix
        '''
        # Return self if the matrix is 1xn or nx1, if it is a diagonal matrix,
        # perform the operation as usual
        if self.get_h_dim() > 1 and self.get_v_dim() > 1:
            content = Matrix.get_row(self, n)
        else:
            content = self
        return content

    def get_col(self, n=0):
        '''(OneDimensionalMatrix) -> OneDimensionalMatrix
        Return self as a column if an attempt is made to retrieve any column
        '''
        # Return self if the matrix is 1xn or n1x, if it is a diagonal matrix,
        # perform the operation as usual
        if self.get_h_dim() > 1 and self.get_v_dim() > 1:
            content = Matrix.get_col(self, n)
        else:
            content = self
        return content


class SquareMatrix(Matrix):
    '''A matrix where the number of rows and columns are equal'''
    def __init__(self, n, default=0):
        '''(SquareMatrix, int, int, float) -> NoneType
        Create a new nxn matrix with all values set to default
        '''
        Matrix.__init__(self, n, n, default)

    def transpose(self):
        '''(SquareMatrix) -> NoneType
        Transpose this matrix
        '''
        # For loop through the upper diagonal values of the matrix and
        # swap the values of m[i,j] with m[j,i]
        for x in range(0, self.get_h_dim()):
            for y in range(x, self.get_v_dim()):
                upper_cor = self.get_val(y, x)
                lower_cor = self.get_val(x, y)
                self.set_val(y, x, lower_cor)
                self.set_val(x, y, upper_cor)

    def get_diagonal(self):
        '''(Squarematrix) -> OneDimensionalMatrix
        Return a one dimensional matrix with the values of the diagonal
        of this matrix
        '''
        # Form a OneDimensional matrix (1xn) with n = dimension of calling
        # matrix.
        ret_mat = OneDimensionalMatrix(self.get_v_dim())
        for i in range(0, self.get_v_dim()):
            ret_mat.set_item(i, self.get_val(i, i))
        return ret_mat

    def set_diagonal(self, new_diagonal):
        '''(SquareMatrix, OneDimensionalMatrix) -> NoneType
        Set the values of the diagonal of this matrix to those of new_diagonal
        '''
        # Raise the MatrixDimensionError if the length of new_diagonal is not
        # equal to the length of the calling matrix
        if new_diagonal.get_h_dim() != self.get_v_dim():
            raise MatrixDimensionError
        # Raise the MatrixInvalidOperationError in the even where new_diagonal
        # is not a OneDimensionalMatrix
        if type(new_diagonal) is OneDimensionalMatrix or\
           type(new_diagonal) is DiagonalMatrix or\
           type(new_diagonal) is IdentityMatrix or\
           types(self) is IdentityMatrix:
            # Determine whether new_diagonal is a row or diagonal matrix
            # For loop through the contents of new_diagonal and set the
            # diagonal values of the calling matrix to the corresponding
            # value
            if new_diagonal.get_v_dim() > 1:
                for i in range(0, new_diagonal.get_v_dim()):
                    self.set_val(i, i, new_diagonal.get_val(i, i))
            else:
                for j in range(0, new_diagonal.get_h_dim()):
                    self.set_val(j, j, new_diagonal.get_val(0, j))
        else:
            raise MatrixInvalidOperationError()


class SymmetricMatrix(SquareMatrix):
    '''A Symmetric Matrix, where m[i, j] = m[j, i] for all i and j'''

    def set_val(self, i, j, new_val):
        '''(SymmetricMatrix, int, int, float) -> NoneType
        Set the value of m[i, j] and m[j, i] to new_val for this matrix m
        REQ: i and j must be indices of the calling matrix
        '''
        # If i and j are not indices of the calling matrix, raise
        # MatrixIndexError
        if i > self.get_v_dim() or j > self.get_h_dim() or i < 0 or j < 0:
            raise MatrixIndexError
        # Upon setting m[i, j], set m[j, i] also to new_val, if i != j
        Matrix.set_val(self, i, j, new_val)
        if i != j:
            Matrix.set_val(self, j, i, new_val)

    def add_scalar(self, add_value):
        '''(SymmetricMatrix, float) -> NoneType
        Increase all values in this matrix by add_value
        '''
        # Iterate through upper elements and set their values to what they were
        # increase by add_value
        for x in range(0, self.get_h_dim()):
            for y in range(x, self. get_v_dim()):
                self.set_val(y, x, self.get_val(y, x) + add_value)

    def multiply_scalar(self, mult_value):
        '''(SymmetricMatrix, float) -> NoneType
        Multiply all values in this matrix by mult_value
        '''
        # Iterate through all elements and set their values to what they were
        # multiplied by by mult_value
        for x in range(0, self.get_h_dim()):
            for y in range(x, self. get_v_dim()):
                self.set_val(y, x, self.get_val(y, x) * mult_value)


class DiagonalMatrix(SquareMatrix, OneDimensionalMatrix):
    '''A square matrix with 0 values everywhere but the diagonal'''
    def __init__(self, n, default=0):
        '''(DiagonalMatrix, int, int, float) -> NoneType
        Create a new matrix with 0 values everywhere but the diagonal
        '''
        # Create a new square matrix and set its diagonal to default
        SquareMatrix.__init__(self, n, 0)
        for i in range(0, n):
            self.set_val(i, i, default)


class IdentityMatrix(DiagonalMatrix):
    '''A matrix with 1s on the diagonal and 0s everywhere else'''
    def __init__(self, n):
        '''(IdentityMatrix, int) -> NoneType
        Create a nxn matrix with 1s on the diagonal and 0s everywhere else
        REQ: n must be a positive number
        '''
        DiagonalMatrix.__init__(self, n, 1)
