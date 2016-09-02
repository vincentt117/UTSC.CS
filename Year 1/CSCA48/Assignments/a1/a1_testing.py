import a1_design
import unittest


class TestMatrix(unittest.TestCase):
    def test_init(self):
        m_1x1 = a1_design.Matrix([7], [1, 1])
        self.assertTrue(type(m_1x1) == Matrix, "__init__ does not"
                        "create proper object type with int matrices: failed"
                        " to create 1x1 integer holding matrix.")
        txt_m_1x1 = a1_design.Matrix(['a'], [1, 1])
        self.assertTrue(type(txt_m_1x1_2) == Matrix, 
                        "__init__ does not create proper object type with int"
                        "matrices: failed to create 1x1 string holding"
                        "matrix.")
        
        m_1x2 = a1_design.Matrix([1, 2], [1, 2])
        self.assertTrue(type(m_1x2) == Matrix, "__init__ does not"
                        "create proper object type with int matrices: failed"
                        "to create 1x2 integer holding matrix.")
        txt_m_1x2 = a1_design.Matrix(['a', 'b'], [1, 2])
        self.assertTrue(type(txt_m_1x2) == Matrix, "__init__ does not"
                        "create proper object type with int matrices: failed"
                        "to create 1x2 string holding matrix.")
        
        m_2x1 = a1_design.Matrix([1, 2], [2, 1])
        self.assertTrue(type(m_1x2) == Matrix, "__init__ does not"
                        "create proper object type with int matrices: failed"
                        "to create 2x1 integer holding matrix.")
        txt_m_2x1 = a1_design.Matrix(['a', 'b'], [2, 1])
        self.assertTrue(type(txt_m_1x2) == Matrix, "__init__ does not"
                        "create proper object type with int matrices: failed"
                        "to create 2x1 string holding matrix.")
        
        m_2x2_2 = a1_design.Matrix([1, 2, 3, 4], [2, 2])
        self.assertTrue(type(m_2x2) == Matrix, "__init__ does not"
                        "create proper object type with int matrices: failed"
                        "to create 2x2 integer holding matrix.")
        txt_m_2x2_2 = a1_design.Matrix(['a', 'b', 'c', 'd'], [2, 2])
        self.assertTrue(type(txt_m_2x2) == Matrix, "__init__ does not"
                        "create proper object type with int matrices: failed"
                        "to create 2x2 string holding matrix.")

    def test_get_content(self):
        # Test getter method
        # One element matrices
        m_1x1 = a1_design.Matrix([7], [1, 1])
        txt_m_1x1 = a1_design.Matrix(['a'], [1, 1])
        # One by two matrices
        m_1x2 = a1_design.Matrix([1, 2], [1, 2])
        txt_m_1x2 = a1_design.Matrix(['a', 'b'], [1, 2])
        # Two by two (square) matrices that are neither symmetric nor parallel
        m_2x2 = a1_design.Matrix([1, 2, 3, 4], [2, 2])
        txt_m_2x2 = a1_design.Matrix(['a', 'b', 'c', 'd'], [2, 2])
        # Test getter on one by one matrix containing integer only
        self.assertEqual(m_1x1.get_content(), [[7], [1, 1]], "Error"
                         "in retrieval, failure to retrieve content"
                         "of one by one matrix containing integer")
        # Test getter on one by one matrix containing object other integer
        self.assertEqual(txt_m_1x1.get_content(),
                         [['a'], [1, 1]], "Error in retrieval, failure to"
                         "retrieve content of one by one matrix containing"
                         "objects other integers")
        # Test getter on one by two matrix containing integer only
        self.assertEqual(m_1x2.get_content(), [[1, 2], [1, 2]],
                         "Error in retrieval, failure to retrieve content of"
                         "one by two matrix containing integers")
        # Test getter on one by two matrix containing object other integer
        self.assertEqual(txt_m_1x2_1.get_content(),
                         [['a', 'b'], [1, 2]], "Error in retrieval, failure"
                         "to retrieve content of one by two matrix containing"
                         "objects other integers")
        # Test getter on a square matrix containing integer only
        self.assertEqual(m_1x2.get_content(), [[1, 2, 3, 4], [2, 2]],
                         "Error in retrieval, failure to retrieve content of"
                         "two by two matrix containing integers")
        # Test getter on a square matrix containing object other integer
        self.assertEqual(txt_m_1x2_1.get_content(),
                         [['a', 'b', 'c', 'd'], [2, 2]],
                         "Error in retrieval, failure to retrieve content of"
                         "two by two matrix containing objects other than"
                         "integers")

    def test_add_sub(self):
        # One by one numerical summation
        m_1x1_1 = a1_design.Matrix([7], [1, 1])
        m_1x1_2 = a1_design.Matrix([7], [1, 1])
        m_1x1_1.add_sub(m_1x1_2, True)
        self.assertEqual(m_1x1_1.get_content(), [[14], [1, 1]],
                         "Error in operation, summation incorrect")
        m_1x1_3 = a1_design.Matrix([0], [1, 1])
        m_1x1_4 = a1_design.Matrix([0], [1, 1])
        m_1x1_3.add_sub(m_1x1_4, True)
        self.assertEqual(m_1x1_3.get_content(), [[0], [1, 1]],
                         "Error in operation, summation incorrect")
        m_1x1_5 = a1_design.Matrix([7], [1, 1])
        m_1x1_6 = a1_design.Matrix([5], [1, 1])
        m_1x1_5.add_sub(m_1x1_6, True)
        self.assertEqual(m_1x1_5.get_content(), [[12], [1, 1]],
                         "Error in operation, summation incorrect")
        m_1x1_7 = a1_design.Matrix([-3], [1, 1])
        m_1x1_8 = a1_design.Matrix([5], [1, 1])
        m_1x1_7.add_sub(m_1x1_8, True)
        self.assertEqual(m_1x1_7.get_content(), [[2], [1, 1]],
                         "Error in operation, summation incorrect")
        m_1x1_7 = a1_design.Matrix([-2], [1, 1])
        m_1x1_8 = a1_design.Matrix([-3], [1, 1])
        m_1x1_7.add_sub(m_1x1_8, True)
        self.assertEqual(m_1x1_7.get_content(), [[-5], [1, 1]],
                         "Error in operation, summation incorrect")        
        txt_m_1x1_1 = a1_design.Matrix(['a'], [1, 1])
        txt_m_1x1_2 = a1_design.Matrix(['b'], [1, 1])
        txt_m_1x1_1.add_sub(txt_m_1x1_2, True)
        self.assertEqual(m_1x1_1.get_content(), [['ab'], [1, 1]],
                         "Error in operation, summation incorrect")
        txt_m_1x1_3 = a1_design.Matrix(['a'], [1, 1])
        txt_m_1x1_4 = a1_design.Matrix(['a'], [1, 1])
        txt_m_1x1_3.add_sub(txt_m_1x1_4, True)
        self.assertEqual(m_1x1_3.get_content(), [['aa'], [1, 1]],
                         "Error in operation, summation incorrect")
        # One by one numerical subtraction
        m_1x1_9 = a1_design.Matrix([7], [1, 1])
        m_1x1_10 = a1_design.Matrix([7], [1, 1])
        m_1x1_9.add_sub(m_1x1_2, True)
        self.assertEqual(m_1x1_9.get_content(), [[0], [1, 1]],
                         "Error in operation, summation incorrect")
        m_1x1_11 = a1_design.Matrix([0], [1, 1])
        m_1x1_12 = a1_design.Matrix([0], [1, 1])
        m_1x1_11.add_sub(m_1x1_12, True)
        self.assertEqual(m_1x1_11.get_content(), [[0], [1, 1]],
                         "Error in operation, summation incorrect")
        m_1x1_13 = a1_design.Matrix([7], [1, 1])
        m_1x1_14 = a1_design.Matrix([5], [1, 1])
        m_1x1_13.add_sub(m_1x1_14, True)
        self.assertEqual(m_1x1_13.get_content(), [[2], [1, 1]],
                         "Error in operation, summation incorrect")
        m_1x1_15 = a1_design.Matrix([-3], [1, 1])
        m_1x1_16 = a1_design.Matrix([5], [1, 1])
        m_1x1_15.add_sub(m_1x1_16, True)
        self.assertEqual(m_1x1_15.get_content(), [[-8], [1, 1]],
                         "Error in operation, summation incorrect")
        m_1x1_17 = a1_design.Matrix([-2], [1, 1])
        m_1x1_18 = a1_design.Matrix([-3], [1, 1])
        m_1x1_17.add_sub(m_1x1_18, True)
        self.assertEqual(m_1x1_17.get_content(), [[1], [1, 1]],
                         "Error in operation, summation incorrect")      
        # One by two numerical summation
        m_1x2_1 = a1_design.Matrix([1, 2], [1, 2])
        m_1x2_2 = a1_design.Matrix([3, 4], [1, 2])
        m_1x2_1.add_sub(m_1x2_2, True)
        self.assertEqual(txt_m_1x1_1.get_content(), [[4, 6], [1, 2]],
                         "Error in operation, summation incorrect")
        m_1x2_3 = a1_design.Matrix([1, 2], [1, 2])
        m_1x2_4 = a1_design.Matrix([1, 2], [1, 2])
        m_1x2_3.add_sub(m_1x2_4, True)
        self.assertEqual(txt_m_1x1_3.get_content(), [[2, 4], [1, 2]],
                         "Error in operation, summation incorrect")
        m_1x2_5 = a1_design.Matrix([0, 0], [1, 2])
        m_1x2_6 = a1_design.Matrix([0, 0], [1, 2])
        m_1x2_5.add_sub(m_1x2_6, True)
        self.assertEqual(txt_m_1x1_5.get_content(), [[0, 0], [1, 2]],
                         "Error in operation, summation incorrect")
        m_1x2_7 = a1_design.Matrix([5, 7], [1, 2])
        m_1x2_8 = a1_design.Matrix([-3, -2], [1, 2])
        m_1x2_7.add_sub(m_1x2_8, True)
        self.assertEqual(txt_m_1x1_7.get_content(), [[2, 5], [1, 2]],
                         "Error in operation, summation incorrect")
        m_1x2_9 = a1_design.Matrix([-5, -7], [1, 2])
        m_1x2_10 = a1_design.Matrix([3, 2], [1, 2])
        m_1x2_9.add_sub(m_1x2_10, True)
        self.assertEqual(txt_m_1x1_9.get_content(), [[-2, -5], [1, 2]],
                         "Error in operation, summation incorrect")
        m_1x2_11 = a1_design.Matrix([-5, -7], [1, 2])
        m_1x2_12 = a1_design.Matrix([-3, -2], [1, 2])
        m_1x2_11.add_sub(m_1x2_10, True)
        self.assertEqual(txt_m_1x1_9.get_content(), [[-8, -9], [1, 2]],
                         "Error in operation, summation incorrect")
        # One by two string summation   
        txt_m_1x2_1 = a1_design.Matrix(['a', 'b'], [1, 2])
        txt_m_1x2_2 = a1_design.Matrix(['c', 'd'], [1, 2])
        txt_m_1x2_1.add_sub(m_1x2_2, True)
        self.assertEqual(txt_m_1x1_1.get_content(), [['ac', 'bd'], [1, 2]],
                         "Error in operation, summation incorrect")
        txt_m_1x2_1 = a1_design.Matrix(['a', 'a'], [1, 2])
        txt_m_1x2_2 = a1_design.Matrix(['c', 'c'], [1, 2])
        txt_m_1x2_1.add_sub(m_1x2_2, True)
        self.assertEqual(txt_m_1x1_1.get_content(), [['ac', 'ac'], [1, 2]],
                         "Error in operation, summation incorrect")
        # One by two subtraction
        m_1x2_11 = a1_design.Matrix([3, 4], [1, 2])
        m_1x2_12 = a1_design.Matrix([1, 2], [1, 2])
        m_1x2_1.add_sub(m_1x2_12, False)
        self.assertEqual(txt_m_1x1_11.get_content(), [[2, 4], [1, 2]],
                         "Error in operation, subtracton incorrect")
        m_1x2_13 = a1_design.Matrix([1, 2], [1, 2])
        m_1x2_14 = a1_design.Matrix([1, 2], [1, 2])
        m_1x2_13.add_sub(m_1x2_14, True)
        self.assertEqual(txt_m_1x1_13.get_content(), [[0, 0], [0, 0]],
                         "Error in operation, subtraction incorrect")
        m_1x2_15 = a1_design.Matrix([0, 0], [1, 2])
        m_1x2_16 = a1_design.Matrix([0, 0], [1, 2])
        m_1x2_15.add_sub(m_1x2_15, True)
        self.assertEqual(txt_m_1x1_1.get_content(), [[0, 0], [1, 2]],
                         "Error in operation, subtraction incorrect")
        m_1x2_17 = a1_design.Matrix([5, 7], [1, 2])
        m_1x2_18 = a1_design.Matrix([-3, -2], [1, 2])
        m_1x2_17.add_sub(m_1x2_18, True)
        self.assertEqual(txt_m_1x2_17.get_content(), [[2, 5], [1, 2]],
                         "Error in operation, subtracion incorrect")
        m_1x2_19 = a1_design.Matrix([-5, -7], [1, 2])
        m_1x2_20 = a1_design.Matrix([3, 2], [1, 2])
        m_1x2_19.add_sub(m_1x2_20, True)
        self.assertEqual(txt_m_1x1_19.get_content(), [[-8, -9], [1, 2]],
                         "Error in operation, subtraction incorrect")
        m_1x2_21 = a1_design.Matrix([-5, -7], [1, 2])
        m_1x2_22 = a1_design.Matrix([-3, -2], [1, 2])
        m_1x2_21.add_sub(m_1x2_22, True)
        self.assertEqual(txt_m_1x1_21.get_content(), [[-2, -5], [1, 2]],
                         "Error in operation, subtraction incorrect")
        # Two by one numerical summation
        m_2x1_1 = a1_design.Matrix([1, 2], [2, 1])
        m_2x1_2 = a1_design.Matrix([3, 4], [2, 1])
        m_2x1_1.add_sub(m_2x1_2, True)
        self.assertEqual(txt_m_2x1_1.get_content(), [[4, 6], [2, 1]],
                         "Error in operation, addition incorrect")
        m_2x1_3 = a1_design.Matrix([0, 0], [2, 1])
        m_2x1_4 = a1_design.Matrix([0, 0], [2, 1])
        m_2x1_3.add_sub(m_2x1_4, True)
        self.assertEqual(txt_m_2x1_1.get_content(), [[0, 0], [2, 1]],
                         "Error in operation, addition incorrect")
        m_2x1_5 = a1_design.Matrix([1, 2], [2, 1])
        m_2x1_6 = a1_design.Matrix([-4, -2], [2, 1])
        m_2x1_5.add_sub(m_2x1_6, True)
        self.assertEqual(txt_m_2x1_5.get_content(), [[-3, 0], [2, 1]],
                         "Error in operation, addition incorrect")
        m_2x1_7 = a1_design.Matrix([-4, -2], [2, 1])
        m_2x1_8 = a1_design.Matrix([-1, -3], [2, 1])
        m_2x1_7.add_sub(m_2x1_8, True)
        self.assertEqual(txt_m_2x1_7.get_content(), [[-5, -5], [2, 1]],
                         "Error in operation, addition incorrect")
        # Two by one string summation
        txt_m_2x1_1 = a1_design.Matrix(['a', 'b'], [2, 1])
        txt_m_2x1_2 = a1_design.Matrix(['c', 'd'], [2, 1])
        txt_m_2x1_1.add_sub(txt_m_2x1_2, True)
        self.assertEqual(txt_m_2x1_1.get_content(), [['ac', 'bd'], [2, 1]],
                         "Error in operation, addition incorrect")
        txt_m_2x1_3 = a1_design.Matrix(['a', 'a'], [2, 1])
        txt_m_2x1_4 = a1_design.Matrix(['a', 'a'], [2, 1])
        txt_m_2x1_3.add_sub(txt_m_2x1_4, True)
        self.assertEqual(txt_m_2x1_1.get_content(), [['aa', 'aa'], [2, 1]],
                         "Error in operation, addition incorrect")
        txt_m_2x1_3 = a1_design.Matrix(['a', 'b'], [2, 1])
        txt_m_2x1_4 = a1_design.Matrix(['a', 'b'], [2, 1])
        txt_m_2x1_3.add_sub(txt_m_2x1_4, True)
        self.assertEqual(txt_m_2x1_1.get_content(), [['aa', 'bb'], [2, 1]],
                         "Error in operation, addition incorrect")
        # Two by one numerical subtraction
        m_2x1_9 = a1_design.Matrix([3, 4], [2, 1])
        m_2x1_10 = a1_design.Matrix([1, 2], [2, 1])
        m_2x1_9.add_sub(m_2x1_10, True)
        self.assertEqual(txt_m_2x1_9.get_content(), [[2, 2], [2, 1]],
                         "Error in operation, subtraction incorrect")
        m_2x1_11 = a1_design.Matrix([0, 0], [2, 1])
        m_2x1_12 = a1_design.Matrix([0, 0], [2, 1])
        m_2x1_11.add_sub(m_2x1_12, True)
        self.assertEqual(txt_m_2x1_1.get_content(), [[0, 0], [2, 1]],
                         "Error in operation, subtraction incorrect")
        m_2x1_13 = a1_design.Matrix([1, 2], [2, 1])
        m_2x1_14 = a1_design.Matrix([-4, -2], [2, 1])
        m_2x1_13.add_sub(m_2x1_14, True)
        self.assertEqual(txt_m_2x1_13.get_content(), [[5, 0], [2, 1]],
                         "Error in operation, subtraction incorrect")
        m_2x1_15 = a1_design.Matrix([-4, -2], [2, 1])
        m_2x1_16 = a1_design.Matrix([-1, -3], [2, 1])
        m_2x1_15.add_sub(m_2x1_16, True)
        self.assertEqual(txt_m_2x1_7.get_content(), [[-3, 1], [2, 1]],
                         "Error in operation, subtracion incorrect")
        
        # Two by two numerical summation
        m_2x2_1 = a1_design.Matrix([1, 2, 3, 4], [2, 2])
        m_2x2_2 = a1_design.Matrix([5, 6, 7, 8], [2, 2])
        m_2x2_1.add_sub(m_2x2_2, True)
        self.assertEqual(m_2x2_1.get_content, [[6, 8, 10, 12], [2, 2]],
                         "Error in operation, addition incorrect")
        m_2x2_3 = a1_design.Matrix([0, 0, 0, 0], [2, 2])
        m_2x2_4 = a1_design.Matrix([4, 3, 2, 1], [2, 2])
        m_2x2_3.add_sub(m_2x2_4, True)
        self.assertEqual(m_2x2_3.get_content, [[4, 3, 2, 1], [2, 2]],
                         "Error in operation, addition incorrect")
        m_2x2_5 = a1_design.Matrix([0, 0, 0, 0], [2, 2])
        m_2x2_6 = a1_design.Matrix([0, 0, 0, 0], [2, 2])
        m_2x2_5.add_sub(m_2x2_2, True)
        self.assertEqual(m_2x2_1.get_content, [[0, 0, 0, 0], [2, 2]],
                         "Error in operation, addition incorrect")
        m_2x2_7 = a1_design.Matrix([-1, -2, -3, -4], [2, 2])
        m_2x2_8 = a1_design.Matrix([5, 6, 7, 8], [2, 2])
        m_2x2_7.add_sub(m_2x2_8, True)
        self.assertEqual(m_2x2_7.get_content, [[4, 4, 4, 4], [2, 2]],
                         "Error in operation, addition incorrect")
        m_2x2_9 = a1_design.Matrix([-1, -2, -3, -4], [2, 2])
        m_2x2_10 = a1_design.Matrix([-5, -6, -7, -8], [2, 2])
        m_2x2_9.add_sub(m_2x2_2, True)
        self.assertEqual(m_2x2_1.get_content, [[-6, -8, -10, -12], [2, 2]],
                         "Error in operation, addition incorrect")
        # Two by two string summation
        txt_m_2x2_1 = a1_design.Matrix(['a', 'b', 'c', 'd'], [2, 2])
        txt_m_2x2_2 = a1_design.Matrix(['e', 'f', 'g', 'h'], [2, 2])
        txt_m_2x2_1.add_sub(txt_m_2x2_2, True)
        self.assertEqual(m_2x2_1.get_content(),
                         [['ae', 'bf', 'cg', 'dh'], [2, 2]],
                         "Error in operation, summation incorrect")
        txt_m_2x2_3 = a1_design.Matrix(['a', 'a', 'a', 'a'], [2, 2])
        txt_m_2x2_4 = a1_design.Matrix(['b', 'b', 'b', 'b'], [2, 2])
        txt_m_2x2_3.add_sub(txt_m_2x2_4, True)
        self.assertEqual(m_2x2_3.get_content(),
                         [['ab', 'ab', 'ab', 'ab'], [2, 2]],
                         "Error in operation, summation incorrect")
        txt_m_2x2_5 = a1_design.Matrix(['a', 'a', 'a', 'a'], [2, 2])
        txt_m_2x2_6 = a1_design.Matrix(['a', 'a', 'a', 'a'], [2, 2])
        txt_m_2x2_5.add_sub(txt_m_2x2_6, True)
        self.assertEqual(m_2x2_5.get_content(),
                         [['aa', 'aa', 'aa', 'aa'], [2, 2]],
                         "Error in operation, summation incorrect")
        # Two by two nummerical subtraction
        m_2x2_11 = a1_design.Matrix([5, 6, 7, 8], [2, 2])
        m_2x2_12 = a1_design.Matrix([1, 2, 3, 4], [2, 2])
        m_2x2_11.add_sub(m_2x2_2, True)
        self.assertEqual(m_2x2_1.get_content, [[4, 4, 4, 4], [2, 2]],
                         "Error in operation, addition incorrect")
        m_2x2_13 = a1_design.Matrix([1, 2, 3, 4], [2, 2])
        m_2x2_14 = a1_design.Matrix([0, 0, 0, 0], [2, 2])
        m_2x2_13.add_sub(m_2x2_14, True)
        self.assertEqual(m_2x2_3.get_content, [[1, 2, 3, 4], [2, 2]],
                         "Error in operation, addition incorrect")
        m_2x2_15 = a1_design.Matrix([0, 0, 0, 0], [2, 2])
        m_2x2_16 = a1_design.Matrix([1, 2, 3, 4], [2, 2])
        m_2x2_15.add_sub(m_2x2_16, True)
        self.assertEqual(m_2x2_15.get_content, [[-1, -2, -3, -4], [2, 2]],
                         "Error in operation, addition incorrect")
        m_2x2_17 = a1_design.Matrix([1, 2, 3, 4], [2, 2])
        m_2x2_18 = a1_design.Matrix([1, 2, 3, 4], [2, 2])
        m_2x2_17.add_sub(m_2x2_18, True)
        self.assertEqual(m_2x2_17.get_content, [[0, 0, 0, 0], [2, 2]],
                        "Error in operation, addition incorrect")
        m_2x2_19 = a1_design.Matrix([-1, -2, -3, -4], [2, 2])
        m_2x2_20 = a1_design.Matrix([1, 2, 3, 4], [2, 2])
        m_2x2_19.add_sub(m_2x2_20, True)
        self.assertEqual(m_2x2_19.get_content, [[-2, -4, -6, -8], [2, 2]],
                        "Error in operation, addition incorrect")
        m_2x2_21 = a1_design.Matrix([-1, -2, -3, -4], [2, 2])
        m_2x2_20 = a1_design.Matrix([-1, -2, -3, -4], [2, 2])
        m_2x2_21.add_sub(m_2x2_20, True)
        self.assertEqual(m_2x2_19.get_content, [[0, 0, 0, 0], [2, 2]],
                        "Error in operation, addition incorrect")    


    def test_transpose(self):
        # Test the transpose method
        # One by one matrices
        m_1x1 = a1.design.Matrix([1], [1, 1])
        txt_m_1x1 = a1.design.Matrix(['a'], [1, 1])
        # One by two matrices
        m_1x2 = a1_design.Matrix([1, 2], [1, 2])
        txt_m_1x2 = a1_design.Matrix(['a', 'b'], [1, 2])
        # Two by one matrices
        m_2x1_1 = a1_design.Matrix([1, 2], [2, 1])
        txt_m_2x1 = a1_design.Matrix(['a', 'b'], [2, 1])
        # Two by two (square) matrices that are neither symmetric nor parallel
        m_2x2 = a1_design.Matrix([1, 2, 3, 4], [2, 2])
        txt_m_2x2 = a1_design.Matrix(['a', 'b', 'c', 'd'], [2, 2])
        m_1x1.tranpose()
        self.assertEqual(m_1x1.get_content(), [[1], [1, 1]], "Error in"
                         "operation, one by one int tranposition failed")
        txt_m_1x1.transpose()
        self.assertEqual(txt_m_1x1.get_content(), [['a'], [1, 1]], "Error in"
                         "operation, one by one string transposition failed")
        # Transpose one by two matrix containing integers only
        m_1x2.transpose()
        self.assertEqual(m_1x2.get_content(), [[1, 2], [2, 1]],
                         "Error in operation, one by two int transposition"
                         "failed")
        # Transpose one by two matrix containing objects other than integers
        txt_m_1x2.transpose()
        self.assertEqual(txt_two_matrix.get_content(), [['a', 'b'], [2, 1]],
                         "Error in operation, one by two obj tranposition"
                         "failed")
        # Transpose two by one matrix containing integers only
        m_2x1.transpose()
        self.assertEqual(m_2x1.get_content(), [[1, 2], [1, 2]],
                         "Error in operation, two by one int tranposition"
                         "failed")
        # Transpose two by one matrix containing objects other than integers
        txt_m_2x1.transpose()
        self.assertEqual(txt_m_2x1.get_content(), ['a', 'b'], [1, 2],
                         "Error in operation, two by one obj transpoition"
                         "failed")
        # Transpose two by two matrix containing only integers
        m_2x2.transpose()
        self.assertEqual(m_2x2.get_content(), [[1, 3, 2, 4]], [2, 2],
                         "Error in operation, two by two int tranposition"
                         "failed")
        # Transpose two by two matrix containing objects other than integers
        txt_m_2x2.transpose()
        self.assertEqual(txt_m_2x2.get_content(),
                         [['a', 'c', 'b', 'd'], [2, 2]],
                         "Error in operation, two by"
                         "two obj tranposition failed")

    def test_multi(self):
        # Test matrix multiplication
        # One element matrices
        m_1x1_1 = a1_design.Matrix([7], [1, 1])
        m_1x1_2 = a1_design.Matrix([5], [1, 1])
        # One by two matrices
        m_1x2_1 = a1_design.Matrix([1, 2], [1, 2])
        m_1x2_2 = a1_design.Matrix([1, 2], [1, 2])
        # Two by one matrices
        m_2x1 = a1_design.Matrix([3, 4], [2, 1])
        # Two by two (square) matrices that are neither symmetric nor parallel
        m_2x2_1 = a1_design.Matrix([1, 2, 3, 4], [2, 2])
        m_2x2_1 = a1_design.Matrix([5, 6, 7, 8], [2, 2])
        # Test multiplication with one by one matries
        m_1x1_1.multi(m_1x1_2)
        self.assertEqual(m_1x1_1.get_content(), [[35], [1, 1]],
                         "Error in operation, multiplication with one by one"
                         "matrix failed")
        # Test multiplication with one by two matrix and two by one matrix
        m_1x2_1.multi(m_2x1)
        self.assertEqual(m_1x2_1.get_content(), [[5], [1, 1]],
                         "Error in operation, multiplication with one by two"
                         "and two by one matrices failed")
        # Test multiplication with two by one matrix and one by two matrix
        m_2x1.multi(m_1x2_2)
        self.assertEqual(m_2x1.get_content(), [[1, 2, 2, 4], [2, 2]],
                         "Error in operation, multiplcation with two by one"
                         "and one by two matrices failed")
        # Test multiplcation with two two by two (square) matrices
        m_2x2_1.multi(m_2x2_2)
        self.assertEqual(m_2x2_1.get_content(),
                         [[23, 34, 31, 46], [2, 2]], "Error in operation,"
                         " multiplcation with two two by two matrices failed")

    def test_switch(self):
        # Test column/row switching
        m_1x1 = a1_design.Matrix([1], [1, 1])
        m_1x1.switch(True, [1, 1])
        self.assertEqual(m_1x1.get_content(), [[1], [1, 1]],
                         "Error in operation, failure to switch rows")
        m_1x1.switch(False, [1, 1])
        self.assertEqual(m_1x1.get_content(), [[1], [1, 1]],
                         "Error in operation, failure to switch columns")
        txt_m_1x1 = a1_design.Matrix(['a'], [1, 1])
        txt_m_1x1.switch(True, [1, 1])
        self.assertEqual(txt_m_1x1.get_content(), [['a'], [1, 1]],
                         "Error in operation, failure to switch rows")
        txt_m_1x1.switch(False, [1, 1])
        self.assertEqual(txt_m_1x1.get_content(), [['a'], [1, 1]],
                         "Error in operation, failure to switch columns")      
        m_1x2 = a1.design.Matrix([1, 2], [1, 2])
        m_1x2.switch(True, [1, 2])
        self.assertEqual(m_2x2.get_content(), [[2, 1], [1, 2]],
                         "Error in operation, failure to switch rows")
        m_1x2 = a1.design.Matrix([1, 2], [1, 2])
        m_1x2.switch(False, [1, 1])
        self.assertEqual(m_1x2.get_content(), [[1, 2], [1, 2]],
                         "Error in operation, failure to switch rows")
        m_1x2 = a1.design.Matrix(['a', 'b'], [1, 2])
        m_1x2.switch(True, [1, 2])
        self.assertEqual(m_2x2.get_content(), [['b', 'a'], [1, 2]],
                         "Error in operation, failure to switch rows")
        m_1x2 = a1.design.Matrix(['a', 'b'], [1, 2])
        m_1x2.switch(False, [1, 1])
        self.assertEqual(m_1x2.get_content(), [['a', 'b'], [1, 2]],
                         "Error in operation, failure to switch rows")        
        m_2x1 = a1.design.Matrix([1, 2], [2, 1])
        m_2x1.switch(True, [2, 1])
        self.assertEqual(m_2x1.get_content(), [[2, 1], [2, 1]],
                         "Error in operation, failure to switch columns")
        m_2x1 = a1.design.Matrix([1, 2], [2, 1])
        m_2x1.switch(False, [2, 1])
        self.assertEqual(m_2x2.get_content(), [[1, 2], [2, 1]],
                         "Error in operation, failure to switch columns")        
        m_2x1 = a1.design.Matrix(['a', 'b'], [2, 1])
        m_2x1.switch(True, [2, 1])
        self.assertEqual(m_2x1.get_content(), [['b', 'a'], [2, 1]],
                         "Error in operation, failure to switch columns")
        m_2x1 = a1.design.Matrix(['a', 'b'], [2, 1])
        m_2x1.switch(False, [2, 1])
        self.assertEqual(m_2x2.get_content(), [['a', 'b'], [2, 1]],
                         "Error in operation, failure to switch columns")   
        m_2x2 = a1_design.Matrix([1, 2, 3, 4], [2, 2])
        m_2x2.switch(True, [1, 2])
        self.assertEqual(m_2x2.get_content(), [[2, 1, 4, 3], [2, 2]],
                         "Error in operation, failure to switch rows")
        m_2x2.switch(False, [1, 2])
        self.assertEqual(m_2x2.get_content(), [[4, 3, 2, 1], [2, 2]],
                         "Error in operation, failure to switch columns")       
        m_2x2 = a1_design.Matrix(['a', 'b', 'c', 'd'], [2, 2])
        m_2x2.switch(True, [2, 2])
        self.assertEqual(m_2x2.get_content(), [['b', 'a', 'd', 'c'], [2, 2]],
                         "Error in operation, failure to switch rows")
        m_2x2 = a1_design.Matrix(['a', 'b', 'c', 'd'], [2, 2])
        m_2x2.switch(False, [2, 2])
        self.assertEqual(m_2x2.get_content(), [['d', 'c', 'a', 'b'], [2, 2]],
                         "Error in operation, failure to switch columns")

    def test_get_by_row_or_col(self):
        # Test getter by row on 1 by 1 matrix
        m_1x1_1 = a1_design.Matrix([1], [1, 1])
        ret_val = m_1x1_1.get_by_row_or_col([1, 1], True)
        self.assertEqual(ret_val, 1, "Error in getter, failed to retrieve by"
                         "row in one by one matrix")
        m_1x1_2 = a1_design.Matrix([1], [1, 1])
        ret_val = m_1x1_2.get_by_row_or_col([1, 1], False)
        self.assertEqual(ret_val, 1, "Error in getter, failed to retrieve by"
                         "column in one by one matrix")
        txt_m_1x1_1 = a1_design.Matrix(['a'], [1, 1])
        ret_val = txt_m_1x1_1.get_by_row_or_col([1, 1], True)
        self.assertEqual(ret_val, 'a', "Error in getter, failed to retrieve by"
                         "row in one by one matrix")
        txt_m_1x1_2 = a1_design.Matrix(['a'], [1, 1])
        ret_val = txt_m_1x1_2.get_by_row_or_col([1, 1], False)
        self.assertEqual(ret_val, 'a', "Error in getter, failed to retrieve by"
                         "column in one by one matrix")        
        # Test getter by row on 1 by 2 matrix
        m_1x2_1 = a1_design.Matrix([1, 2], [1, 2])
        ret_val = m_1x2_1.get_by_row_or_col([1, 1], True)
        self.assertEqual(ret_val, 1, "Error in getter, failed to retrieve by"
                         "row in one by two matrix")
        m_1x2_2 = a1_design.Matrix([1, 2], [1, 2])
        ret_val = m_1x2_2.get_by_row_or_col([1, 2], True)
        self.assertEqual(ret_val, 2, "Error in getter, failed to retrieve by"
                         "row in one by two matrix")
        m_1x2_3 = a1_design.Matrix([1, 2], [1, 2])
        ret_val = m_1x2_3.get_by_row_or_col([1, 1], False)
        self.assertEqual(ret_val, 1, "Error in getter, failed to retrieve by"
                         "column in one by two matrix")
        m_1x2_4 = a1_design.Matrix([1, 2], [1, 2])
        ret_val = m_1x2.get_by_row_or_col([2, 1], False)
        self.assertEqual(ret_val, 2, "Error in getter, failed to retrieve by"
                         "column in one by two matrix")
        
        txt_m_1x2_1 = a1_design.Matrix(['a', 'b'], [1, 2])
        ret_val = txt_m_1x2_1.get_by_row_or_col([1, 1], True)
        self.assertEqual(ret_val, 'a', "Error in getter, failed to retrieve by"
                         "row in one by two matrix")
        txt_m_1x2_2 = a1_design.Matrix(['a', 'b'], [1, 2])
        ret_val = txt_m_1x2_1.get_by_row_or_col([1, 2], True)
        self.assertEqual(ret_val, 'b', "Error in getter, failed to retrieve by"
                         "row in one by two matrix")
        txt_m_1x2_3 = a1_design.Matrix(['a' 'b'], [1, 2])
        ret_val = txt_m_1x2_3.get_by_row_or_col([1, 1], False)
        self.assertEqual(ret_val, 'a', "Error in getter, failed to retrieve by"
                         "column in one by two matrix")
        txt_m_1x2_4 = a1_design.Matrix(['a' 'b'], [1, 2])
        ret_val = txt_m_1x2_4.get_by_row_or_col([2, 1], False)
        self.assertEqual(ret_val, 'b', "Error in getter, failed to retrieve by"
                         "column in one by two matrix")        
        # Test getter by row on 2 by 1 matrix
        m_2x1_1 = a1_design.Matrix([1, 2], [2, 1])
        ret_val = m_1x2.get_by_row_or_col([1, 1], True)
        self.assertEqual(ret_val, 1, "Error in getter, failed to retrieve by"
                         "row in two by one matrix")
        m_2x1_2 = a1_design.Matrix([1, 2], [2, 1])
        ret_val = m_1x2_2.get_by_row_or_col([2, 1], True)
        self.assertEqual(ret_val, 2, "Error in getter, failed to retrieve by"
                         "column in twp by one matrix")
        m_2x1_3 = a1_design.Matrix([1, 2], [2, 1])
        ret_val = m_1x2_3.get_by_row_or_col([1, 1], False)
        self.assertEqual(ret_val, 1, "Error in getter, failed to retrieve by"
                         "row in two by one matrix")
        m_2x1_4 = a1_design.Matrix([1, 2], [2, 1])
        ret_val = m_1x2_4.get_by_row_or_col([1, 2], True)
        self.assertEqual(ret_val, 2, "Error in getter, failed to retrieve by"
                         "column in twp by one matrix")        
        txt_2x1_1 = a1_design.Matrix(['a', 'b'], [2, 1])
        ret_val = m_1x2.get_by_row_or_col([1, 1], True)
        self.assertEqual(ret_val, 'a', "Error in getter, failed to retrieve by"
                         "row in two by one matrix")
        txt_2x1_2 = a1_design.Matrix(['a', 'b'], [2, 1])
        ret_val = txt_2x1_2.get_by_row_or_col([2, 1], True)
        self.assertEqual(ret_val, 'b', "Error in getter, failed to retrieve by"
                         "column in twp by one matrix")
        txt_2x1_3 = a1_design.Matrix(['a', 'b'], [2, 1])
        ret_val = txt_m_1x2_3.get_by_row_or_col([1, 1], False)
        self.assertEqual(ret_val, 'a', "Error in getter, failed to retrieve by"
                         "row in two by one matrix")
        txt_2x1_4 = a1_design.Matrix(['a', 'b'], [2, 1])
        ret_val = txt_m_1x2_4.get_by_row_or_col([1, 2], True)
        self.assertEqual(ret_val, 'b', "Error in getter, failed to retrieve by"
                         "column in two by one matrix")        
        # Test getter by row on 2 by 2 (square) matrix
        m_2x2_1 = a1_design.Matrix([1, 2, 3, 4], [2, 2])
        ret_val = m_2x2_1.get_by_row_or_col([1, 1], True)
        self.assertEqual(ret_val, 1, "Error in getter, failed to retrieve by"
                         "row")
        m_2x2_2 = a1_design.Matrix([1, 2, 3, 4], [2, 2])
        ret_val = m_2x2_2.get_by_row_or_col([1, 2], True)
        self.assertEqual(ret_val, 3, "Error in getter, failed to retrieve by"
                         "row")
        m_2x2_3 = a1_design.Matrix([1, 2, 3, 4], [2, 2])
        ret_val = m_2x2_3.get_by_row_or_col([2, 1], True)
        self.assertEqual(ret_val, 2, "Error in getter, failed to retrieve by"
                         "row")
        m_2x2_4 = a1_design.Matrix([1, 2, 3, 4], [2, 2])
        ret_val = m_2x2_4.get_by_row_or_col([2, 2], True)
        self.assertEqual(ret_val, 4, "Error in getter, failed to retrieve by"
                         "row")
        m_2x2_5 = a1_design.Matrix([1, 2, 3, 4], [2, 2])
        ret_val = m_2x2_5.get_by_row_or_col([1, 1], False)
        self.assertEqual(ret_val, 1, "Error in getter, failed to retrieve by"
                         "column")
        m_2x2_6 = a1_design.Matrix([1, 2, 3, 4], [2, 2])
        ret_val = m_2x2_6.get_by_row_or_col([1, 2], False)
        self.assertEqual(ret_val, 2, "Error in getter, failed to retrieve by"
                         "column")
        m_2x2_7 = a1_design.Matrix([1, 2, 3, 4], [2, 2])
        ret_val = m_2x2_7.get_by_row_or_col([2, 1], False)
        self.assertEqual(ret_val, 3, "Error in getter, failed to retrieve by"
                         "column")
        m_2x2_8 = a1_design.Matrix([1, 2, 3, 4], [2, 2])
        ret_val = m_2x2_8.get_by_row_or_col([2, 2], False)
        self.assertEqual(ret_val, 4, "Error in getter, failed to retrieve by"
                         "column")        
        txt_m_2x2_1 = a1_design.Matrix(['a', 'b', 'c', 'd'], [2, 2])
        ret_val = txt_m_2x2_1.get_by_row_or_col([1, 1], True)
        self.assertEqual(ret_val, 'a', "Error in getter, failed to retrieve by"
                         "row")
        txt_m_2x2_2 = a1_design.Matrix(['a', 'b', 'c', 'd'], [2, 2])
        ret_val = txt_m_2x2_2.get_by_row_or_col([1, 2], True)
        self.assertEqual(ret_val, 'c', "Error in getter, failed to retrieve by"
                         "row")
        txt_m_2x2_3 = a1_design.Matrix(['a', 'b', 'c', 'd'], [2, 2])
        ret_val = txt_m_2x2_3.get_by_row_or_col([2, 1], True)
        self.assertEqual(ret_val, 'b', "Error in getter, failed to retrieve by"
                         "row")
        txt_m_2x2_4 = a1_design.Matrix(['a', 'b', 'c', 'd'], [2, 2])
        ret_val = txt_m_2x2_4.get_by_row_or_col([2, 2], True)
        self.assertEqual(ret_val, 'd', "Error in getter, failed to retrieve by"
                         "row")
        txt_m_2x2_5 = a1_design.Matrix(['a', 'b', 'c', 'd'], [2, 2])
        ret_val = txt_m_2x2_5.get_by_row_or_col([1, 1], False)
        self.assertEqual(ret_val, 'a', "Error in getter, failed to retrieve by"
                         "column")
        txt_m_2x2_6 = a1_design.Matrix(['a', 'b', 'c', 'd'], [2, 2])
        ret_val = txt_m_2x2.get_by_row_or_col([1, 2], False)
        self.assertEqual(ret_val, 'b', "Error in getter, failed to retrieve by"
                         "column")
        txt_m_2x2_7 = a1_design.Matrix(['a', 'b', 'c', 'd'], [2, 2])
        ret_val = txt_m_2x2_7.get_by_row_or_col([2, 1], False)
        self.assertEqual(ret_val, 'c', "Error in getter, failed to retrieve by"
                         "column")
        txt_m_2x2_8 = a1_design.Matrix(['a', 'b', 'c', 'd'], [2, 2])
        ret_val = txt_m_2x2_8.get_by_row_or_col([2, 2], False)
        self.assertEqual(ret_val, 'd', "Error in getter, failed to retrieve by"
                         "column")
        
    def test_set_by_row_col(self):
        # Test setter by row on 1 by 1 matrix
        m_1x1_1 = a1_design.Matrix([1], [1, 1])
        m_1x1_1.set_by_row_or_col(2, [1, 1], True)
        self.assertEqual(m_1x1_1.get_content(), [[2], [1, 1]],
                         "Error in setter, failed to set by"
                         "row in one by one matrix")
        m_1x1_2 = a1_design.Matrix([1], [1, 1])
        m_1x1_2.set_by_row_or_col(2, [1, 1], False)
        self.assertEqual(m_1x1_2.get_content(), [[2], [1, 1]],
                         "Error in setter, failed to set by"
                         "column in one by one matrix")
        txt_m_1x1_1 = a1_design.Matrix(['a'], [1, 1])
        txt_m_1x1_1.set_by_row_or_col('b', [1, 1], True)
        self.assertEqual(txt_m_1x1_1.get_content(), [['b'], [1, 1]],
                         "Error in setter, failed to set by"
                         "row in one by one matrix")
        txt_m_1x1_2 = a1_design.Matrix(['a'], [1, 1])
        txt_m_1x1_2.set_by_row_or_col('b', [1, 1], False)
        self.assertEqual(txt_m_1x1_2.get_content(), [[2], [1, 1]],
                         "Error in setter, failed to set by"
                         "column in one by one matrix") 
        # Test setter by row on 1 by 2 matrix
        m_1x2_1 = a1_design.Matrix([1, 2], [1, 2])
        m_1x2_1.set_by_row_or_col(3, [1, 1], True)
        self.assertEqual(m_1x2_1.get_content(), [[3, 2], [1, 2]],
                         "Error in setter, failed to set by"
                         "row in one by two matrix")
        m_1x2_2 = a1_design.Matrix([1, 2], [1, 2])
        m_1x2_2.set_by_row_or_col(3, [1, 2], True)
        self.assertEqual(m_1x2_2.get_content(), [[1, 3], [1, 2]],
                         "Error in setter, failed to set by"
                         "row in one by two matrix")
        m_1x2_3 = a1_design.Matrix([1, 2], [1, 2])
        m_1x2_3.set_by_row_or_col(3, [1, 1], False)
        self.assertEqual(m_1x2_3.get_content(), [[3, 2], [1, 2]],
                         "Error in setter, failed to set by"
                         "column in one by two matrix")
        m_1x2_4 = a1_design.Matrix([1, 2], [1, 2])
        m_1x2_4.set_by_row_or_col(3, [2, 1], False)
        self.assertEqual(m_1x2_4.get_content(), [[1, 3], [1, 2]],
                         "Error in setter, failed to set by"
                         "column in one by two matrix")
        txt_m_1x2_1 = a1_design.Matrix(['a', 'b'], [1, 2])
        m_1x2.set_by_row_or_col('c', [1, 1], True)
        self.assertEqual(txt_m_1x2_1.get_content(), [['c', 'b'], [1, 2]],
                         "Error in setter, failed to set by"
                         "row in one by two matrix")
        txt_m_1x2_2.set_by_row_or_col('c', [1, 2], True)
        self.assertEqual(txt_m_1x2_2.get_content(), [['a', 'c'], [1, 2]],
                         "Error in setter, failed to set by"
                         "row in one by two matrix")        
        txt_m_1x2_3 = a1_design.Matrix(['a', 'b'], [1, 2])
        txt_m_1x2_3.set_by_row_or_col('c', [1, 1], False)
        self.assertEqual(txt_m_1x2_3.get_content(), [['c', 'b'], [1, 2]],
                         "Error in setter, failed to set by"
                         "column in one by two matrix")
        m_1x2_4 = a1_design.Matrix([1, 2], [1, 2])
        txt_m_1x2_4.set_by_row_or_col('c', [1, 2], False)
        self.assertEqual(xt_m_1x2_4.get_content(), [['a' 'c'], [1, 2]],
                         "Error in setter, failed to set by"
                         "column in one by two matrix")
        # Test setter by row on 2 by 1 matrix
        m_2x1_1 = a1_design.Matrix([1, 2], [2, 1])
        m_2x1.set_by_row_or_col(3, [1, 1], True)
        self.assertEqual(m_2x1.get_content(), [[3, 2], [2, 1]],
                         "Error in setter, failed to set by"
                         "row in two by one matrix")
        m_2x1_1 = a1_design.Matrix([1, 2], [2, 1])
        m_2x1.set_by_row_or_col(3, [2, 1], True)
        self.assertEqual(m_2x1.get_content(), [[1, 3], [2, 1]],
                         "Error in setter, failed to set by"
                         "row in two by one matrix")
        m_2x1 = a1_design.Matrix([1, 1], [2, 1])
        m_2x1.set_by_row_or_col(3, [1, 1], False)
        self.assertEqual(m_2x1.get_content(), [[3, 2], [2, 1]],
                         "Error in setter, failed to retrieve by"
                         "column in one by two matrix")
        m_2x1.set_by_row_or_col(3, [1, 2], False)
        self.assertEqual(m_2x1.get_content(), [[1, 3], [2, 1]],
                         "Error in setter, failed to retrieve by"
                         "column in one by two matrix")
        m_2x1 = a1_design.Matrix(['a', 'b'], [2, 1])
        m_2x1.set_by_row_or_col('c', [1, 1], True)
        self.assertEqual(m_2x1.get_content(), [['c', 'b'], [2, 1]],
                         "Error in setter, failed to set by"
                         "row in two by one matrix")
        m_2x1.set_by_row_or_col('c', [2, 1], True)
        self.assertEqual(m_2x1.get_content(), [['a', 'c'], [2, 1]],
                         "Error in setter, failed to set by"
                         "row in two by one matrix")
        m_2x1 = a1_design.Matrix(['a', 'b'], [2, 1])
        m_2x1.set_by_row_or_col('c', [1, 1], False)
        self.assertEqual(m_2x1.get_content(), [['c', 'b'], [2, 1]],
                         "Error in setter, failed to retrieve by"
                         "column in two by one matrix")
        m_2x1.set_by_row_or_col('c', [1, 2], False)
        self.assertEqual(m_2x1.get_content(), [['a', 'c'], [2, 1]],
                         "Error in setter, failed to retrieve by"
                         "column in two by one matrix")      
        # Test setter by row on 2 by 2 (square) matrix
        m_2x2_1 = a1_design.Matrix([1, 2, 3, 4], [2, 2])
        m_2x2_1.set_by_row_or_col(7, [1, 1], True)
        self.assertEqual(m_2x2_1.get_content(),[[7, 2, 3, 4], [2, 2]],
                         "Error in setter, failed to retrieve by"
                         "row in two by two matrix")
        m_2x2_2 = a1_design.Matrix([1, 2, 3, 4], [2, 2])
        m_2x2_2.set_by_row_or_col(7, [1, 2], True)
        self.assertEqual(m_2x2_2.get_content(),[[1, 2, 7, 4], [2, 2]],
                         "Error in setter, failed to retrieve by"
                         "row in two by two matrix")
        m_2x2_3 = a1_design.Matrix([1, 2, 3, 4], [2, 2])
        m_2x2_3.set_by_row_or_col(7, [2, 1], True)
        self.assertEqual(m_2x2_3.get_content(),[[1, 7, 3, 4], [2, 2]],
                         "Error in setter, failed to retrieve by"
                         "row in two by two matrix")
        m_2x2_4 = a1_design.Matrix([1, 2, 3, 4], [2, 2])
        m_2x2_4.set_by_row_or_col(7, [2, 2], True)
        self.assertEqual(m_2x2_4.get_content(),[[1, 2, 3, 4], [2, 2]],
                         "Error in setter, failed to retrieve by"
                         "row in two by two matrix")        
        m_2x2_5 = a1_design.Matrix([1, 2, 3, 4], [2, 2])
        m_2x2_5.set_by_row_or_col(7, [1, 1], False)
        self.assertEqual(m_2x2_5.get_content(),[[7, 2, 3, 4], [2, 2]],
                         "Error in setter, failed to retrieve by"
                         "column in two by two matrix")
        m_2x2_6 = a1_design.Matrix([1, 2, 3, 4], [2, 2])
        m_2x2_6.set_by_row_or_col(7, [1, 2], False)
        self.assertEqual(m_2x2_6.get_content(),[[1, 7, 3, 4], [2, 2]],
                         "Error in setter, failed to retrieve by"
                         "column in two by two matrix") 
        m_2x2_7 = a1_design.Matrix([1, 2, 3, 4], [2, 2])
        m_2x2_7.set_by_row_or_col(7, [2, 1], False)        
        self.assertEqual(m_2x2_5.get_content(),[[1, 2, 7, 4], [2, 2]],
                         "Error in setter, failed to retrieve by"
                         "column in two by two matrix")
        m_2x2_8 = a1_design.Matrix([1, 2, 3, 4], [2, 2])
        m_2x2_8.set_by_row_or_col(7, [2, 2], False)
        self.assertEqual(m_2x2_5.get_content(),[[1, 2, 3, 7], [2, 2]],
                         "Error in setter, failed to retrieve by"
                         "column in two by two matrix")
        # Test setter by row on 2 by 2 (square) matrix
        m_2x2_1 = a1_design.Matrix(['a', 'b', 'c', 'd'], [2, 2])
        m_2x2_1.set_by_row_or_col('x', [1, 1], True)
        self.assertEqual(m_2x2_1.get_content(),[['x', 'b', 'c', 'd'], [2, 2]],
                         "Error in setter, failed to retrieve by"
                         "row in two by two matrix")
        m_2x2_2 = a1_design.Matrix(['a', 'b', 'c', 'd'], [2, 2])
        m_2x2_2.set_by_row_or_col('x', [1, 2], True)
        self.assertEqual(m_2x2_2.get_content(),[['a', 'b', 'x', 'd'], [2, 2]],
                         "Error in setter, failed to retrieve by"
                         "row in two by two matrix")
        m_2x2_3 = a1_design.Matrix(['a', 'b', 'c', 'd'], [2, 2])
        m_2x2_3.set_by_row_or_col('x', [2, 1], True)
        self.assertEqual(m_2x2_3.get_content(),[['a', 'x', 'c', 'd'], [2, 2]],
                         "Error in setter, failed to retrieve by"
                         "row in two by two matrix")
        m_2x2_4 = a1_design.Matrix(['a', 'b', 'c', 'd'], [2, 2])
        m_2x2_4.set_by_row_or_col('x', [2, 2], True)
        self.assertEqual(m_2x2_4.get_content(),[['a', 'b', 'c', 'x'], [2, 2]],
                         "Error in setter, failed to retrieve by"
                         "row in two by two matrix")        
        m_2x2_5 = a1_design.Matrix(['a', 'b', 'c', 'd'], [2, 2])
        m_2x2_5.set_by_row_or_col('x', [1, 1], False)
        self.assertEqual(m_2x2_5.get_content(),[['x', 'b', 'c', 'd'], [2, 2]],
                         "Error in setter, failed to retrieve by"
                         "column in two by two matrix")
        m_2x2_6 = a1_design.Matrix(['a', 'b', 'c', 'd'], [2, 2])
        m_2x2_6.set_by_row_or_col('x', [1, 2], False)
        self.assertEqual(m_2x2_6.get_content(),[['a', 'x', 'c', 'd'], [2, 2]],
                         "Error in setter, failed to retrieve by"
                         "column in two by two matrix") 
        m_2x2_7 = a1_design.Matrix(['a', 'b', 'c', 'd'], [2, 2])
        m_2x2_7.set_by_row_or_col('x', [2, 1], False)        
        self.assertEqual(m_2x2_5.get_content(),[['a', 'b', 'c', 'd'], [2, 2]],
                         "Error in setter, failed to retrieve by"
                         "column in two by two matrix")
        m_2x2_8 = a1_design.Matrix(['a', 'b', 'c', 'd'], [2, 2])
        m_2x2_8.set_by_row_or_col('x', [2, 2], False)
        self.assertEqual(m_2x2_5.get_content(),[['a', 'b', 'c', 'd'], [2, 2]],
                         "Error in setter, failed to retrieve by"
                         "column in two by two matrix")

    def test_get_determinant(self):
        # Test get determinant method (applicable to only 2 by 2 matrices)
        m_2x2_1 = a1_design.Matrix([0, 0, 0, 0], [2, 2])
        deter = m_2x2_1.get_determinant()
        self.assertEqual(deter, 0, "Error in operation, failed to form"
                         "determinant")
        m_2x2_2 = a1_design.Matrix([3, 4, 8, 6], [2, 2])
        deter = m_2x2_2.get_determinant()
        self.assertEqual(deter, -14, "Error in operation, failed to form"
                         "determinant")
        m_2x2_3 = a1_design.Matrix([1, 1, 1, 1], [2, 2])
        deter = m_2x2_3.get_determinant()
        self.assertEqual(deter, 0, "Error in operation, failed to form"
                         "determinant")


class TestSquareMatrix(unittest.TestCase):
    def test_square_m_init(self):
        m_1x1 = a1_design.SquareMatrix([7], [1, 1])
        self.assertTrue(type(m_1x1) == SquareMatrix,
                        "__init__ does not create proper object type with int"
                        "matrices")
        m_1x1_2 = a1_design.SquareMatrix(['a'], [1, 1])
        self.assertTrue(type(m_1x1_2) == SquareMatrix, "__init__ does"
                        "not create proper object type with int matrices")
        m_1x1 = a1_design.SquareMatrix([1, 2, 3, 4], [2, 2])
        self.assertTrue(type(m_1x1) == SquareMatrix,
                        "__init__ does not create proper object type with int"
                        "matrices")
        m_1x1_2 = a1_design.SquareMatrix(['a', 'b', 'c', 'd'],
                                                  [2, 2])
        self.assertTrue(type(m_1x1_2) == SquareMatrix, "__init__ does"
                        "not create proper object type with int matrices")

    def test_square_m_get_content(self):
        # Test getter method
        self.assertEqual(m_1x1.get_content(), [[1], [1, 1]],
                         "Error in retrieval, failure to retrieve content of"
                         "two by two matrix containing integers")
        txt_m_1x1 = a1_design.SquareMatrix(['a'], [1, 1])
        self.assertEqual(m_1x1.get_content(), [['a'], [1, 1]],
                         "Error in retrieval, failure to retrieve content of"
                         "two by two matrix containing integers")
        m_2x2 = a1_design.SquareMatrix([1, 2, 2, 1], [2, 2])
        self.assertEqual(m_2x2.get_content(), [[1, 2, 2, 1], [2, 2]],
                         "Error in retrieval, failure to retrieve content of"
                         "two by two matrix containing integers")
        txt_m_2x2 = a1_design.SquareMatrix(['a', 'b', 'c', 'd'], [2, 2])
        self.assertEqual(txt_m_1x2_1.get_content(),
                         [['a', 'b', 'c', 'd'], [2, 2]],
                         "Error in retrieval, failure to retrieve content of"
                         "two by two matrix containing objects other than"
                         "integers")

    def test_square_m_add_sub(self):
        m_1x1_1 = a1_design.SquareMatrix([7], [1, 1])
        m_1x1_2 = a1_design.SquareMatrix([7], [1, 1])
        m_1x1_1.add_sub(m_1x1_2, True)
        self.assertEqual(m_1x1_1.get_content(), [[14], [1, 1]],
                         "Error in operation, summation incorrect")
        m_1x1_3 = a1_design.SquareMatrix([0], [1, 1])
        m_1x1_4 = a1_design.SquareMatrix([0], [1, 1])
        m_1x1_3.add_sub(m_1x1_4, True)
        self.assertEqual(m_1x1_3.get_content(), [[0], [1, 1]],
                         "Error in operation, summation incorrect")
        m_1x1_5 = a1_design.SquareMatrix([7], [1, 1])
        m_1x1_6 = a1_design.SquareMatrix([5], [1, 1])
        m_1x1_5.add_sub(m_1x1_6, True)
        self.assertEqual(m_1x1_5.get_content(), [[12], [1, 1]],
                         "Error in operation, summation incorrect")
        m_1x1_7 = a1_design.SquareMatrix([-3], [1, 1])
        m_1x1_8 = a1_design.SquareMatrix([5], [1, 1])
        m_1x1_7.add_sub(m_1x1_8, True)
        self.assertEqual(m_1x1_7.get_content(), [[2], [1, 1]],
                         "Error in operation, summation incorrect")
        m_1x1_7 = a1_design.SquareMatrix([-2], [1, 1])
        m_1x1_8 = a1_design.SquareMatrix([-3], [1, 1])
        m_1x1_7.add_sub(m_1x1_8, True)
        self.assertEqual(m_1x1_7.get_content(), [[-5], [1, 1]],
                         "Error in operation, summation incorrect")        
        txt_m_1x1_1 = a1_design.SquareMatrix(['a'], [1, 1])
        txt_m_1x1_2 = a1_design.SquareMatrix(['b'], [1, 1])
        txt_m_1x1_1.add_sub(txt_m_1x1_2, True)
        self.assertEqual(m_1x1_1.get_content(), [['ab'], [1, 1]],
                         "Error in operation, summation incorrect")
        txt_m_1x1_3 = a1_design.SquareMatrix(['a'], [1, 1])
        txt_m_1x1_4 = a1_design.SquareMatrix(['a'], [1, 1])
        txt_m_1x1_3.add_sub(txt_m_1x1_4, True)
        self.assertEqual(m_1x1_3.get_content(), [['aa'], [1, 1]],
                         "Error in operation, summation incorrect")
        # One by one numerical subtraction
        m_1x1_9 = a1_design.SquareMatrix([7], [1, 1])
        m_1x1_10 = a1_design.SquareMatrix([7], [1, 1])
        m_1x1_9.add_sub(m_1x1_2, False)
        self.assertEqual(m_1x1_9.get_content(), [[0], [1, 1]],
                         "Error in operation, subtraction incorrect")
        m_1x1_11 = a1_design.SquareMatrix([0], [1, 1])
        m_1x1_12 = a1_design.SquareMatrix([0], [1, 1])
        m_1x1_11.add_sub(m_1x1_12, False)
        self.assertEqual(m_1x1_11.get_content(), [[0], [1, 1]],
                         "Error in operation, subtraction incorrect")
        m_1x1_13 = a1_design.SquareMatrix([7], [1, 1])
        m_1x1_14 = a1_design.SquareMatrix([5], [1, 1])
        m_1x1_13.add_sub(m_1x1_14, False)
        self.assertEqual(m_1x1_13.get_content(), [[2], [1, 1]],
                         "Error in operation, subtraction incorrect")
        m_1x1_15 = a1_design.SquareMatrix([-3], [1, 1])
        m_1x1_16 = a1_design.SquareMatrix([5], [1, 1])
        m_1x1_15.add_sub(m_1x1_16, False)
        self.assertEqual(m_1x1_15.get_content(), [[-8], [1, 1]],
                         "Error in operation, subtraction incorrect")
        m_1x1_17 = a1_design.SquareMatrix([-2], [1, 1])
        m_1x1_18 = a1_design.SquareMatrix([-3], [1, 1])
        m_1x1_17.add_sub(m_1x1_18, False)
        self.assertEqual(m_1x1_17.get_content(), [[1], [1, 1]],
                         "Error in operation, Subtraction incorrect")
        # Two by two numerical summation
        m_2x2_1 = a1_design.SquareMatrix([1, 2, 3, 4], [2, 2])
        m_2x2_2 = a1_design.SquareMatrix([5, 6, 7, 8], [2, 2])
        m_2x2_1.add_sub(m_2x2_2, True)
        self.assertEqual(m_2x2_1.get_content, [[6, 8, 10, 12], [2, 2]],
                         "Error in operation, addition incorrect")
        m_2x2_3 = a1_design.SquareMatrix([0, 0, 0, 0], [2, 2])
        m_2x2_4 = a1_design.SquareMatrix([4, 3, 2, 1], [2, 2])
        m_2x2_3.add_sub(m_2x2_4, True)
        self.assertEqual(m_2x2_3.get_content, [[4, 3, 2, 1], [2, 2]],
                         "Error in operation, addition incorrect")
        m_2x2_5 = a1_design.SquareMatrix([0, 0, 0, 0], [2, 2])
        m_2x2_6 = a1_design.SquareMatrix([0, 0, 0, 0], [2, 2])
        m_2x2_5.add_sub(m_2x2_2, True)
        self.assertEqual(m_2x2_1.get_content, [[0, 0, 0, 0], [2, 2]],
                         "Error in operation, addition incorrect")
        m_2x2_7 = a1_design.SquareMatrix([-1, -2, -3, -4], [2, 2])
        m_2x2_8 = a1_design.SquareMatrix([5, 6, 7, 8], [2, 2])
        m_2x2_7.add_sub(m_2x2_8, True)
        self.assertEqual(m_2x2_7.get_content, [[4, 4, 4, 4], [2, 2]],
                         "Error in operation, addition incorrect")
        m_2x2_9 = a1_design.SquareMatrix([-1, -2, -3, -4], [2, 2])
        m_2x2_10 = a1_design.SquareMatrix([-5, -6, -7, -8], [2, 2])
        m_2x2_9.add_sub(m_2x2_2, True)
        self.assertEqual(m_2x2_1.get_content, [[-6, -8, -10, -12], [2, 2]],
                         "Error in operation, addition incorrect")
        # Two by two string summation
        txt_m_2x2_1 = a1_design.SquareMatrix(['a', 'b', 'c', 'd'], [2, 2])
        txt_m_2x2_2 = a1_design.SquareMatrix(['e', 'f', 'g', 'h'], [2, 2])
        txt_m_2x2_1.add_sub(txt_m_2x2_2, True)
        self.assertEqual(m_2x2_1.get_content(),
                         [['ae', 'bf', 'cg', 'dh'], [2, 2]],
                         "Error in operation, summation incorrect")
        txt_m_2x2_3 = a1_design.SquareMatrix(['a', 'a', 'a', 'a'], [2, 2])
        txt_m_2x2_4 = a1_design.SquareMatrix(['b', 'b', 'b', 'b'], [2, 2])
        txt_m_2x2_3.add_sub(txt_m_2x2_4, True)
        self.assertEqual(m_2x2_3.get_content(),
                         [['ab', 'ab', 'ab', 'ab'], [2, 2]],
                         "Error in operation, summation incorrect")
        txt_m_2x2_5 = a1_design.SquareMatrix(['a', 'a', 'a', 'a'], [2, 2])
        txt_m_2x2_6 = a1_design.SquareMatrix(['a', 'a', 'a', 'a'], [2, 2])
        txt_m_2x2_5.add_sub(txt_m_2x2_6, True)
        self.assertEqual(m_2x2_5.get_content(),
                         [['aa', 'aa', 'aa', 'aa'], [2, 2]],
                         "Error in operation, summation incorrect")
        # Two by two nummerical subtraction
        m_2x2_11 = a1_design.SquareMatrix([5, 6, 7, 8], [2, 2])
        m_2x2_12 = a1_design.SquareMatrix([1, 2, 3, 4], [2, 2])
        m_2x2_11.add_sub(m_2x2_2, False)
        self.assertEqual(m_2x2_1.get_content, [[4, 4, 4, 4], [2, 2]],
                         "Error in operation, subtraction incorrect")
        m_2x2_13 = a1_design.SquareMatrix([1, 2, 3, 4], [2, 2])
        m_2x2_14 = a1_design.SquareMatrix([0, 0, 0, 0], [2, 2])
        m_2x2_13.add_sub(m_2x2_14, False)
        self.assertEqual(m_2x2_3.get_content, [[1, 2, 3, 4], [2, 2]],
                         "Error in operation, addition incorrect")
        m_2x2_15 = a1_design.SquareMatrix([0, 0, 0, 0], [2, 2])
        m_2x2_16 = a1_design.SquareMatrix([1, 2, 3, 4], [2, 2])
        m_2x2_15.add_sub(m_2x2_16, False)
        self.assertEqual(m_2x2_15.get_content, [[-1, -2, -3, -4], [2, 2]],
                         "Error in operation, subtraction incorrect")
        m_2x2_17 = a1_design.SquareMatrix([1, 2, 3, 4], [2, 2])
        m_2x2_18 = a1_design.SquareMatrix([1, 2, 3, 4], [2, 2])
        m_2x2_17.add_sub(m_2x2_18, False)
        self.assertEqual(m_2x2_17.get_content, [[0, 0, 0, 0], [2, 2]],
                        "Error in operation, subtraction incorrect")
        m_2x2_19 = a1_design.SquareMatrix([-1, -2, -3, -4], [2, 2])
        m_2x2_20 = a1_design.SquareMatrix([1, 2, 3, 4], [2, 2])
        m_2x2_19.add_sub(m_2x2_20, False)
        self.assertEqual(m_2x2_19.get_content, [[-2, -4, -6, -8], [2, 2]],
                        "Error in operation, subtraction incorrect")
        m_2x2_21 = a1_design.SquareMatrix([-1, -2, -3, -4], [2, 2])
        m_2x2_20 = a1_design.SquareMatrix([-1, -2, -3, -4], [2, 2])
        m_2x2_21.add_sub(m_2x2_20, False)
        self.assertEqual(m_2x2_19.get_content, [[0, 0, 0, 0], [2, 2]],
                        "Error in operation, subtraction incorrect")

    def test_square_m_transpose(self):
        m_1x1.transpose()
        m_1x1 = a1_design.SquareMatrix([1], [1, 1])
        self.assertEqual(m_1x1.get_content(), [[1], [1, 1]], "Error"
                         "in operation, one by one int tranposition failed.")
        txt_m_1x1.transpose()
        txt_m_1x1 = a1_design.SquareMatrix(['a'], [1, 1])
        self.assertEqual(txt_m_1x1.get_content(), [['a'], [1, 1]], 
                         "Error in operation, one by one int tranposition"
                         "failed.")
        # Transpose two by two matrix containing only integers
        m_2x2.transpose()
        m_2x2 = a1_design.SquareMatrix([1, 2, 3, 4], [2, 2])
        self.assertEqual(m_2x2.get_content(), [[1, 3, 2, 4]], [2, 2],
                         "Error in operation, two by two int tranposition"
                         "failed")
        # Transpose two by two matrix containing objects other than integers
        m_2x2.transpose()
        txt_m_2x2 = a1_design.SquareMatrix(['a', 'b', 'c', 'd'], [2, 2])
        self.assertEqual(txt_m_2x2.get_content(),
                         [['a', 'c', 'b', 'd']], "Error in operation, two by"
                         "two obj tranposition failed")

    def test_square_m_multi(self):
        # Test matrix multiplication
        m_1x1_1 = a1_design.SquareMatrix([0], [1, 1])
        m_1x1_2 = a1_design.SquareMatrix([1], [1, 1])
        m_1x1_3 = a1_design.SquareMatrix([2], [1, 1])
        m_1x1_4 = a1_design.SquareMatrix([2], [1, 1])
        # Two by two (square) matrices that are neither symmetric nor parallel
        m_2x2_1 = a1_design.SquareMatrix([1, 2, 3, 4], [2, 2])
        m_2x2_2 = a1_design.SquareMatrix([5, 6, 7, 8], [2, 2])

        # Test multiplication with one by one matries
        m_1x1_1.multi(m_1x1_2)
        self.assertEqual(m_1x1_1.get_content(), [[0], [1, 1]],
                         "Error in operation, multiplication with one by one"
                         "matrix failed")
        # Test multiplication with one by two matrix and two by one matrix
        m_1x2_2.multi(m_1x1_3)
        self.assertEqual(m_1x2_1.get_content(), [[2], [1, 1]],
                         "Error in operation, multiplication with one by two"
                         "and two by one matrices failed")
        # Test multiplication with two by one matrix and one by two matrix
        m_2x1.multi(m_1x2_2)
        self.assertEqual(m_2x1.get_content(), [[1, 2, 2, 4], [2, 2]],
                         "Error in operation, multiplcation with two by one"
                         "and one by two matrices failed")
        # Test multiplcation with two two by two (square) matrices
        m_2x2_1.multi(m_2x2_2)
        self.assertEqual(m_2x2_1.get_content(),
                         [[23, 34, 31, 46], [2, 2]], "Error in operation,"
                         " multiplcation with two two by two matrices failed")

    def test_square_m_switch(self):
        m_1x1 = a1_design.Matrix([1], [1, 1])
        m_1x1.switch(True, [1, 1])
        self.assertEqual(m_1x1.get_content(), [[1], [1, 1]],
                         "Error in operation, failure to switch rows")
        m_1x1.switch(False, [1, 1])
        self.assertEqual(m_1x1.get_content(), [[1], [1, 1]],
                         "Error in operation, failure to switch columns")
        txt_m_1x1 = a1_design.Matrix(['a'], [1, 1])
        txt_m_1x1.switch(True, [1, 1])
        self.assertEqual(txt_m_1x1.get_content(), [['a'], [1, 1]],
                         "Error in operation, failure to switch rows")
        txt_m_1x1.switch(False, [1, 1])
        self.assertEqual(txt_m_1x1.get_content(), [['a'], [1, 1]],
                         "Error in operation, failure to switch columns")      
        m_2x2 = a1_design.Matrix([1, 2, 3, 4], [2, 2])
        m_2x2.switch(True, [1, 2])
        self.assertEqual(m_2x2.get_content(), [[2, 1, 4, 3], [2, 2]],
                         "Error in operation, failure to switch rows")
        m_2x2.switch(False, [1, 2])
        self.assertEqual(m_2x2.get_content(), [[4, 3, 2, 1], [2, 2]],
                         "Error in operation, failure to switch columns")       
        m_2x2 = a1_design.Matrix(['a', 'b', 'c', 'd'], [2, 2])
        m_2x2.switch(True, [2, 2])
        self.assertEqual(m_2x2.get_content(), [['b', 'a', 'd', 'c'], [2, 2]],
                         "Error in operation, failure to switch rows")
        m_2x2 = a1_design.Matrix(['a', 'b', 'c', 'd'], [2, 2])
        m_2x2.switch(False, [2, 2])
        self.assertEqual(m_2x2.get_content(), [['d', 'c', 'a', 'b'], [2, 2]],
                         "Error in operation, failure to switch columns")

    def test_square_m_get_by_row_or_col(self):
        m_1x1_1 = a1_design.Matrix([1], [1, 1])
        ret_val = m_1x1_1.get_by_row_or_col([1, 1], True)
        self.assertEqual(ret_val, 1, "Error in getter, failed to retrieve by"
                         "row in one by one matrix")
        m_1x1_2 = a1_design.Matrix([1], [1, 1])
        ret_val = m_1x1_2.get_by_row_or_col([1, 1], False)
        self.assertEqual(ret_val, 1, "Error in getter, failed to retrieve by"
                         "column in one by one matrix")
        txt_m_1x1_1 = a1_design.Matrix(['a'], [1, 1])
        ret_val = txt_m_1x1_1.get_by_row_or_col([1, 1], True)
        self.assertEqual(ret_val, 'a', "Error in getter, failed to retrieve by"
                         "row in one by one matrix")
        txt_m_1x1_2 = a1_design.Matrix(['a'], [1, 1])
        ret_val = txt_m_1x1_2.get_by_row_or_col([1, 1], False)
        self.assertEqual(ret_val, 'a', "Error in getter, failed to retrieve by"
                         "column in one by one matrix")
       # Test getter by row on 2 by 2 (square) matrix
        m_2x2_1 = a1_design.Matrix([1, 2, 3, 4], [2, 2])
        ret_val = m_2x2_1.get_by_row_or_col([1, 1], True)
        self.assertEqual(ret_val, 1, "Error in getter, failed to retrieve by"
                         "row")
        m_2x2_2 = a1_design.Matrix([1, 2, 3, 4], [2, 2])
        ret_val = m_2x2_2.get_by_row_or_col([1, 2], True)
        self.assertEqual(ret_val, 3, "Error in getter, failed to retrieve by"
                         "row")
        m_2x2_3 = a1_design.Matrix([1, 2, 3, 4], [2, 2])
        ret_val = m_2x2_3.get_by_row_or_col([2, 1], True)
        self.assertEqual(ret_val, 2, "Error in getter, failed to retrieve by"
                         "row")
        m_2x2_4 = a1_design.Matrix([1, 2, 3, 4], [2, 2])
        ret_val = m_2x2_4.get_by_row_or_col([2, 2], True)
        self.assertEqual(ret_val, 4, "Error in getter, failed to retrieve by"
                         "row")
        m_2x2_5 = a1_design.Matrix([1, 2, 3, 4], [2, 2])
        ret_val = m_2x2_5.get_by_row_or_col([1, 1], False)
        self.assertEqual(ret_val, 1, "Error in getter, failed to retrieve by"
                         "column")
        m_2x2_6 = a1_design.Matrix([1, 2, 3, 4], [2, 2])
        ret_val = m_2x2_6.get_by_row_or_col([1, 2], False)
        self.assertEqual(ret_val, 2, "Error in getter, failed to retrieve by"
                         "column")
        m_2x2_7 = a1_design.Matrix([1, 2, 3, 4], [2, 2])
        ret_val = m_2x2_7.get_by_row_or_col([2, 1], False)
        self.assertEqual(ret_val, 3, "Error in getter, failed to retrieve by"
                         "column")
        m_2x2_8 = a1_design.Matrix([1, 2, 3, 4], [2, 2])
        ret_val = m_2x2_8.get_by_row_or_col([2, 2], False)
        self.assertEqual(ret_val, 4, "Error in getter, failed to retrieve by"
                         "column")        
        txt_m_2x2_1 = a1_design.Matrix(['a', 'b', 'c', 'd'], [2, 2])
        ret_val = txt_m_2x2_1.get_by_row_or_col([1, 1], True)
        self.assertEqual(ret_val, 'a', "Error in getter, failed to retrieve by"
                         "row")
        txt_m_2x2_2 = a1_design.Matrix(['a', 'b', 'c', 'd'], [2, 2])
        ret_val = txt_m_2x2_2.get_by_row_or_col([1, 2], True)
        self.assertEqual(ret_val, 'c', "Error in getter, failed to retrieve by"
                         "row")
        txt_m_2x2_3 = a1_design.Matrix(['a', 'b', 'c', 'd'], [2, 2])
        ret_val = txt_m_2x2_3.get_by_row_or_col([2, 1], True)
        self.assertEqual(ret_val, 'b', "Error in getter, failed to retrieve by"
                         "row")
        txt_m_2x2_4 = a1_design.Matrix(['a', 'b', 'c', 'd'], [2, 2])
        ret_val = txt_m_2x2_4.get_by_row_or_col([2, 2], True)
        self.assertEqual(ret_val, 'd', "Error in getter, failed to retrieve by"
                         "row")
        txt_m_2x2_5 = a1_design.Matrix(['a', 'b', 'c', 'd'], [2, 2])
        ret_val = txt_m_2x2_5.get_by_row_or_col([1, 1], False)
        self.assertEqual(ret_val, 'a', "Error in getter, failed to retrieve by"
                         "column")
        txt_m_2x2_6 = a1_design.Matrix(['a', 'b', 'c', 'd'], [2, 2])
        ret_val = txt_m_2x2.get_by_row_or_col([1, 2], False)
        self.assertEqual(ret_val, 'b', "Error in getter, failed to retrieve by"
                         "column")
        txt_m_2x2_7 = a1_design.Matrix(['a', 'b', 'c', 'd'], [2, 2])
        ret_val = txt_m_2x2_7.get_by_row_or_col([2, 1], False)
        self.assertEqual(ret_val, 'c', "Error in getter, failed to retrieve by"
                         "column")
        txt_m_2x2_8 = a1_design.Matrix(['a', 'b', 'c', 'd'], [2, 2])
        ret_val = txt_m_2x2_8.get_by_row_or_col([2, 2], False)
        self.assertEqual(ret_val, 'd', "Error in getter, failed to retrieve by"
                         "column")

    def test_square_m_set_by_row_col(self):
        # Test setter by row on 1 by 1 matrix
        m_1x1_1 = a1_design.Matrix([1], [1, 1])
        m_1x1_1.set_by_row_or_col(2, [1, 1], True)
        self.assertEqual(m_1x1_1.get_content(), [[2], [1, 1]],
                         "Error in setter, failed to set by"
                         "row in one by one matrix")
        m_1x1_2 = a1_design.Matrix([1], [1, 1])
        m_1x1_2.set_by_row_or_col(2, [1, 1], False)
        self.assertEqual(m_1x1_2.get_content(), [[2], [1, 1]],
                         "Error in setter, failed to set by"
                         "column in one by one matrix")
        txt_m_1x1_1 = a1_design.Matrix(['a'], [1, 1])
        txt_m_1x1_1.set_by_row_or_col('b', [1, 1], True)
        self.assertEqual(txt_m_1x1_1.get_content(), [['b'], [1, 1]],
                         "Error in setter, failed to set by"
                         "row in one by one matrix")
        txt_m_1x1_2 = a1_design.Matrix(['a'], [1, 1])
        txt_m_1x1_2.set_by_row_or_col('b', [1, 1], False)
        self.assertEqual(txt_m_1x1_2.get_content(), [[2], [1, 1]],
                         "Error in setter, failed to set by"
                         "column in one by one matrix") 
        # Test setter by row on 2 by 2 (square) matrix
        m_2x2_1 = a1_design.Matrix([1, 2, 3, 4], [2, 2])
        m_2x2_1.set_by_row_or_col(7, [1, 1], True)
        self.assertEqual(m_2x2_1.get_content(),[[7, 2, 3, 4], [2, 2]],
                         "Error in setter, failed to retrieve by"
                         "row in two by two matrix")
        m_2x2_2 = a1_design.Matrix([1, 2, 3, 4], [2, 2])
        m_2x2_2.set_by_row_or_col(7, [1, 2], True)
        self.assertEqual(m_2x2_2.get_content(),[[1, 2, 7, 4], [2, 2]],
                         "Error in setter, failed to retrieve by"
                         "row in two by two matrix")
        m_2x2_3 = a1_design.Matrix([1, 2, 3, 4], [2, 2])
        m_2x2_3.set_by_row_or_col(7, [2, 1], True)
        self.assertEqual(m_2x2_3.get_content(),[[1, 7, 3, 4], [2, 2]],
                         "Error in setter, failed to retrieve by"
                         "row in two by two matrix")
        m_2x2_4 = a1_design.Matrix([1, 2, 3, 4], [2, 2])
        m_2x2_4.set_by_row_or_col(7, [2, 2], True)
        self.assertEqual(m_2x2_4.get_content(),[[1, 2, 3, 4], [2, 2]],
                         "Error in setter, failed to retrieve by"
                         "row in two by two matrix")        
        m_2x2_5 = a1_design.Matrix([1, 2, 3, 4], [2, 2])
        m_2x2_5.set_by_row_or_col(7, [1, 1], False)
        self.assertEqual(m_2x2_5.get_content(),[[7, 2, 3, 4], [2, 2]],
                         "Error in setter, failed to retrieve by"
                         "column in two by two matrix")
        m_2x2_6 = a1_design.Matrix([1, 2, 3, 4], [2, 2])
        m_2x2_6.set_by_row_or_col(7, [1, 2], False)
        self.assertEqual(m_2x2_6.get_content(),[[1, 7, 3, 4], [2, 2]],
                         "Error in setter, failed to retrieve by"
                         "column in two by two matrix") 
        m_2x2_7 = a1_design.Matrix([1, 2, 3, 4], [2, 2])
        m_2x2_7.set_by_row_or_col(7, [2, 1], False)        
        self.assertEqual(m_2x2_5.get_content(),[[1, 2, 7, 4], [2, 2]],
                         "Error in setter, failed to retrieve by"
                         "column in two by two matrix")
        m_2x2_8 = a1_design.Matrix([1, 2, 3, 4], [2, 2])
        m_2x2_8.set_by_row_or_col(7, [2, 2], False)
        self.assertEqual(m_2x2_5.get_content(),[[1, 2, 3, 7], [2, 2]],
                         "Error in setter, failed to retrieve by"
                         "column in two by two matrix")
        # Test setter by row on 2 by 2 (square) matrix
        m_2x2_1 = a1_design.Matrix(['a', 'b', 'c', 'd'], [2, 2])
        m_2x2_1.set_by_row_or_col('x', [1, 1], True)
        self.assertEqual(m_2x2_1.get_content(),[['x', 'b', 'c', 'd'], [2, 2]],
                         "Error in setter, failed to retrieve by"
                         "row in two by two matrix")
        m_2x2_2 = a1_design.Matrix(['a', 'b', 'c', 'd'], [2, 2])
        m_2x2_2.set_by_row_or_col('x', [1, 2], True)
        self.assertEqual(m_2x2_2.get_content(),[['a', 'b', 'x', 'd'], [2, 2]],
                         "Error in setter, failed to retrieve by"
                         "row in two by two matrix")
        m_2x2_3 = a1_design.Matrix(['a', 'b', 'c', 'd'], [2, 2])
        m_2x2_3.set_by_row_or_col('x', [2, 1], True)
        self.assertEqual(m_2x2_3.get_content(),[['a', 'x', 'c', 'd'], [2, 2]],
                         "Error in setter, failed to retrieve by"
                         "row in two by two matrix")
        m_2x2_4 = a1_design.Matrix(['a', 'b', 'c', 'd'], [2, 2])
        m_2x2_4.set_by_row_or_col('x', [2, 2], True)
        self.assertEqual(m_2x2_4.get_content(),[['a', 'b', 'c', 'x'], [2, 2]],
                         "Error in setter, failed to retrieve by"
                         "row in two by two matrix")        
        m_2x2_5 = a1_design.Matrix(['a', 'b', 'c', 'd'], [2, 2])
        m_2x2_5.set_by_row_or_col('x', [1, 1], False)
        self.assertEqual(m_2x2_5.get_content(),[['x', 'b', 'c', 'd'], [2, 2]],
                         "Error in setter, failed to retrieve by"
                         "column in two by two matrix")
        m_2x2_6 = a1_design.Matrix(['a', 'b', 'c', 'd'], [2, 2])
        m_2x2_6.set_by_row_or_col('x', [1, 2], False)
        self.assertEqual(m_2x2_6.get_content(),[['a', 'x', 'c', 'd'], [2, 2]],
                         "Error in setter, failed to retrieve by"
                         "column in two by two matrix") 
        m_2x2_7 = a1_design.Matrix(['a', 'b', 'c', 'd'], [2, 2])
        m_2x2_7.set_by_row_or_col('x', [2, 1], False)        
        self.assertEqual(m_2x2_5.get_content(),[['a', 'b', 'c', 'd'], [2, 2]],
                         "Error in setter, failed to retrieve by"
                         "column in two by two matrix")
        m_2x2_8 = a1_design.Matrix(['a', 'b', 'c', 'd'], [2, 2])
        m_2x2_8.set_by_row_or_col('x', [2, 2], False)
        self.assertEqual(m_2x2_5.get_content(),[['a', 'b', 'c', 'd'], [2, 2]],
                         "Error in setter, failed to retrieve by"
                         "column in two by two matrix")

    def test_square_m_get_determinant(self):
         # Test get determinant method (applicable to only 2 by 2 matrices)
        m_2x2_1 = a1_design.Matrix([0, 0, 0, 0], [2, 2])
        deter = m_2x2_1.get_determinant()
        self.assertEqual(deter, 0, "Error in operation, failed to form"
                         "determinant")
        m_2x2_2 = a1_design.Matrix([3, 4, 8, 6], [2, 2])
        deter = m_2x2_2.get_determinant()
        self.assertEqual(deter, -14, "Error in operation, failed to form"
                         "determinant")
        m_2x2_3 = a1_design.Matrix([1, 1, 1, 1], [2, 2])
        deter = m_2x2_3.get_determinant()
        self.assertEqual(deter, 0, "Error in operation, failed to form"
                         "determinant")


    def test_square_m_get_by_diag(self):
        # Test getter by index at diagonal
        m_1x1_1 = a1_design.SquareMatrix([1], [1, 1])
        ret_val = m_1x1_1.get_by_diag(1)
        self.assertEqual(ret_val, 1, "Error in operation, failed to retrieve"
                         "by diagonal in the square matrix")
        txt_m_1x1_1 = a1_design.SquareMatrix(['a'], [1, 1])
        ret_val = txt_m_1x1_1.get_by_diag(1)
        self.assertEqual(ret_val, 'a', "Error in operation, failed to retrieve"
                         "by diagonal in the square matrix")       
        m_2x2_1 = a1_design.SquareMatrix([1, 2, 3, 4], [2, 2])
        ret_val = m_2x2_1.get_by_diag(1)
        self.assertEqual(ret_val, 1, "Error in operation, failed to retrieve"
                         "by diagonal in the square matrix")
        m_2x2_2 = a1_design.SquareMatrix([1, 2, 3, 4], [2, 2])
        ret_val = m_2x2_2.get_by_diag(2)
        self.assertEqual(ret_val, 4, "Error in operation, failed to retrieve"
                         "by diagonal in the square matrix")
        txt_m_2x2_1 = a1_design.SquareMatrix(['a', 'b', 'c', 'd'], [2, 2])
        ret_val = m_2x2_1.get_by_diag(1)
        self.assertEqual(ret_val, 'a', "Error in operation, failed to retrieve"
                         "by diagonal in the square matrix")        
        txt_m_2x2_2 = a1_design.SquareMatrix(['a', 'b', 'c', 'd'], [2, 2])
        ret_val = m_2x2_2.get_by_diag(2)
        self.assertEqual(ret_val, 'd', "Error in operation, failed to retrieve"
                         "by diagonal in the square matrix")

    def test_square_m_set_by_diag(self):
        m_1x1_1 = a1_design.SquareMatrix([1], [1])
        m_1x1_1.set_by_diag(7, 1)
        self.assertEqual(m_1x1_1.get_content(), [[7], [1]],
                        "Error in operation, failed to set"
                         "by diagonal in the square matrix")
        m_1x1_1 = a1_design.SquareMatrix(['a'], [1, 1])
        m_1x1_1.set_by_diag('b', 1)
        self.assertEqual(m_2x2_1.get_content(), [['b'], [1, 1]],
                        "Error in operation, failed to set"
                         "by diagonal in the square matrix")         
        # Test getter by index at diagonal
        m_2x2_1 = a1_design.SquareMatrix([1, 2, 3, 4], [2, 2])
        m_2x2_1.set_by_diag(7, 1)
        self.assertEqual(m_2x2_1.get_content(), [[7, 2, 3, 4], [2, 2]],
                        "Error in operation, failed to set"
                         "by diagonal in the square matrix")
        m_2x2_2 = a1_design.SquareMatrix([1, 2, 3, 4], [2, 2])
        m_2x2_2.set_by_diag(7, 2)
        self.assertEqual(m_2x2_1.get_content(), [[1, 2, 3, 7], [2, 2]],
                        "Error in operation, failed to set"
                         "by diagonal in the square matrix")
        m_2x2_1 = a1_design.SquareMatrix(['a', 'b', 'c', 'd'], [2, 2])
        m_2x2_1.set_by_diag('x', 1)
        self.assertEqual(m_2x2_1.get_content(), [['x', 'b', 'c', 'd'], [2, 2]],
                        "Error in operation, failed to set"
                         "by diagonal in the square matrix")
        m_2x2_2 = a1_design.SquareMatrix(['a', 'b', 'c', 'd'], [2, 2])
        m_2x2_2.set_by_diag('x', 2)
        self.assertEqual(m_2x2_1.get_content(), [['a', 'b', 'c', 'x'], [2, 2]],
                        "Error in operation, failed to set"
                         "by diagonal in the square matrix")




class TestSymmetricMatrix(unittest.TestCase):
    def test_symm_m_init(self):
        m_1x1 = a1_design.Symmetric([7], [1, 1])
        self.assertTrue(type(m_1x1) == Symmetric,
                        "__init__ does not create proper object type with int"
                        "matrices")
        txt_m_1x1 = a1_design.Symmetric(['a'], [1, 1])
        self.assertTrue(type(txt_m_1x1_2) == Symmetric, "__init__ does"
                        "not create proper object type with int matrices")
        m_2x2 = a1_design.Symmetric([1, 2, 2, 1], [2, 2])
        self.assertTrue(type(txt_m_1x1) == Symmetric,
                        "__init__ does not create proper object type with int"
                        "matrices")
        txt_m_2x2 = a1_design.Symmetric(['a', 'b', 'b', 'a'], 2, 2])
        self.assertTrue(type(m_2x2) == Symmetric, "__init__ does"
                        "not create proper object type with int matrices")

    def test_symm_get_content(self):
        # Test getter method
        m_1x1 = a1_design.Symmetric([1], [1, 1])
        self.assertEqual(m_1x1.get_content(), [[1], [1, 1]],
                         "Error in retrieval, failure to retrieve content of"
                         "two by two matrix containing integers")
        txt_m_1x1 = a1_design.Symmetric(['a'], [1, 1])
        self.assertEqual(m_1x1.get_content(), [['a'], [1, 1]],
                         "Error in retrieval, failure to retrieve content of"
                         "two by two matrix containing integers")
        m_2x2 = a1_design.Symmetric([1, 2, 2, 1], [2, 2])
        self.assertEqual(m_1x2.get_content(), [[1, 2, 2, 1], [2, 2]],
                         "Error in retrieval, failure to retrieve content of"
                         "two by two matrix containing integers")
        txt_m_1x1 = a1_design.Symmetric(['a', 'b', 'b', 'a'], [2, 2])
        self.assertEqual(txt_m_1x2_1.get_content(),
                         [['a', 'b', 'b', 'a'], [2, 2]],
                         "Error in retrieval, failure to retrieve content of"
                         "two by two matrix containing objects other than"
                         "integers")

    def test_symm_m_add_sub(self):
        # One by one numerical summation
        m_1x1_1 = a1_design.SymmetricMatrix([7], [1, 1])
        m_1x1_2 = a1_design.SymmetricMatrix([7], [1, 1])
        m_1x1_1.add_sub(m_1x1_2, True)
        self.assertEqual(m_1x1_1.get_content(), [[14], [1, 1]],
                         "Error in operation, summation incorrect")
        m_1x1_3 = a1_design.SymmetricMatrix([0], [1, 1])
        m_1x1_4 = a1_design.SymmetricMatrix([0], [1, 1])
        m_1x1_3.add_sub(m_1x1_4, True)
        self.assertEqual(m_1x1_3.get_content(), [[0], [1, 1]],
                         "Error in operation, summation incorrect")
        m_1x1_5 = a1_design.SymmetricMatrix([7], [1, 1])
        m_1x1_6 = a1_design.SymmetricMatrix([5], [1, 1])
        m_1x1_5.add_sub(m_1x1_6, True)
        self.assertEqual(m_1x1_5.get_content(), [[12], [1, 1]],
                         "Error in operation, summation incorrect")
        m_1x1_7 = a1_design.SymmetricMatrix([-3], [1, 1])
        m_1x1_8 = a1_design.SymmetricMatrix([5], [1, 1])
        m_1x1_7.add_sub(m_1x1_8, True)
        self.assertEqual(m_1x1_7.get_content(), [[2], [1, 1]],
                         "Error in operation, summation incorrect")
        m_1x1_7 = a1_design.SymmetricMatrix([-2], [1, 1])
        m_1x1_8 = a1_design.SymmetricMatrix([-3], [1, 1])
        m_1x1_7.add_sub(m_1x1_8, True)
        self.assertEqual(m_1x1_7.get_content(), [[-5], [1, 1]],
                         "Error in operation, summation incorrect")        
        txt_m_1x1_1 = a1_design.SymmetricMatrix(['a'], [1, 1])
        txt_m_1x1_2 = a1_design.SymmetricMatrix(['b'], [1, 1])
        txt_m_1x1_1.add_sub(txt_m_1x1_2, True)
        self.assertEqual(m_1x1_1.get_content(), [['ab'], [1, 1]],
                         "Error in operation, summation incorrect")
        txt_m_1x1_3 = a1_design.SymmetricMatrix(['a'], [1, 1])
        txt_m_1x1_4 = a1_design.SymmetricMatrix(['a'], [1, 1])
        txt_m_1x1_3.add_sub(txt_m_1x1_4, True)
        self.assertEqual(m_1x1_3.get_content(), [['aa'], [1, 1]],
                         "Error in operation, summation incorrect")
        # One by one numerical subtraction
        m_1x1_9 = a1_design.SymmetricMatrix([7], [1, 1])
        m_1x1_10 = a1_design.SymmetricMatrix([7], [1, 1])
        m_1x1_9.add_sub(m_1x1_2, True)
        self.assertEqual(m_1x1_9.get_content(), [[0], [1, 1]],
                         "Error in operation, summation incorrect")
        m_1x1_11 = a1_design.SymmetricMatrix([0], [1, 1])
        m_1x1_12 = a1_design.SymmetricMatrix([0], [1, 1])
        m_1x1_11.add_sub(m_1x1_12, True)
        self.assertEqual(m_1x1_11.get_content(), [[0], [1, 1]],
                         "Error in operation, summation incorrect")
        m_1x1_13 = a1_design.SymmetricMatrix([7], [1, 1])
        m_1x1_14 = a1_design.SymmetricMatrix([5], [1, 1])
        m_1x1_13.add_sub(m_1x1_14, True)
        self.assertEqual(m_1x1_13.get_content(), [[2], [1, 1]],
                         "Error in operation, summation incorrect")
        m_1x1_15 = a1_design.SymmetricMatrix([-3], [1, 1])
        m_1x1_16 = a1_design.SymmetricMatrix([5], [1, 1])
        m_1x1_15.add_sub(m_1x1_16, True)
        self.assertEqual(m_1x1_15.get_content(), [[-8], [1, 1]],
                         "Error in operation, summation incorrect")
        m_1x1_17 = a1_design.SymmetricMatrix([-2], [1, 1])
        m_1x1_18 = a1_design.SymmetricMatrix([-3], [1, 1])
        m_1x1_17.add_sub(m_1x1_18, True)
        self.assertEqual(m_1x1_17.get_content(), [[1], [1, 1]],
                         "Error in operation, summation incorrect")
        # Two by two numerical summation
        m_2x2_1 = a1_design.SymmetricMatrix([1, 2, 2, 1], [2, 2])
        m_2x2_2 = a1_design.SymmetricMatrix([3, 4, 4, 3], [2, 2])
        m_2x2_1.add_sub(m_2x2_2, True)
        self.assertEqual(m_2x2_1.get_content, [[4, 6, 6, 4], [2, 2]],
                         "Error in operation, addition incorrect")
        m_2x2_3 = a1_design.SymmetricMatrix([0, 0, 0, 0], [2, 2])
        m_2x2_4 = a1_design.SymmetricMatrix([1, 2, 2, 1], [2, 2])
        m_2x2_3.add_sub(m_2x2_4, True)
        self.assertEqual(m_2x2_3.get_content, [[1, 2, 2, 1], [2, 2]],
                         "Error in operation, addition incorrect")
        m_2x2_5 = a1_design.SymmetricMatrix([0, 0, 0, 0], [2, 2])
        m_2x2_6 = a1_design.SymmetricMatrix([0, 0, 0, 0], [2, 2])
        m_2x2_5.add_sub(m_2x2_2, True)
        self.assertEqual(m_2x2_1.get_content, [[0, 0, 0, 0], [2, 2]],
                         "Error in operation, addition incorrect")
        m_2x2_7 = a1_design.SymmetricMatrix([-1, -2, -2, -1], [2, 2])
        m_2x2_8 = a1_design.SymmetricMatrix([1, 2, 2, 1,], [2, 2])
        m_2x2_7.add_sub(m_2x2_8, True)
        self.assertEqual(m_2x2_7.get_content, [[0, 0, 0, 0], [2, 2]],
                         "Error in operation, addition incorrect")
        m_2x2_9 = a1_design.SymmetricMatrix([-1, -2, -2, -1], [2, 2])
        m_2x2_10 = a1_design.SymmetricMatrix([-3, -4, -4, -3], [2, 2])
        m_2x2_9.add_sub(m_2x2_2, True)
        self.assertEqual(m_2x2_9.get_content, [[-4, -6, -6, -4], [2, 2]],
                         "Error in operation, addition incorrect")
        # Two by two string summation
        txt_m_2x2_1 = a1_design.SymmetricMatrix(['a', 'b', 'b', 'a'], [2, 2])
        txt_m_2x2_2 = a1_design.SymmetricMatrix(['d', 'c', 'c', 'd'], [2, 2])
        txt_m_2x2_1.add_sub(txt_m_2x2_2, True)
        self.assertEqual(m_2x2_1.get_content(),
                         [['ad', 'bc', 'bc', 'ad'], [2, 2]],
                         "Error in operation, summation incorrect")
        txt_m_2x2_3 = a1_design.SymmetricMatrix(['a', 'a', 'a', 'a'], [2, 2])
        txt_m_2x2_4 = a1_design.SymmetricMatrix(['b', 'b', 'b', 'b'], [2, 2])
        txt_m_2x2_3.add_sub(txt_m_2x2_4, True)
        self.assertEqual(m_2x2_3.get_content(),
                         [['ab', 'ab', 'ab', 'ab'], [2, 2]],
                         "Error in operation, summation incorrect")
        txt_m_2x2_5 = a1_design.SymmetricMatrix(['a', 'a', 'a', 'a'], [2, 2])
        txt_m_2x2_6 = a1_design.SymmetricMatrix(['a', 'a', 'a', 'a'], [2, 2])
        txt_m_2x2_5.add_sub(txt_m_2x2_6, True)
        self.assertEqual(m_2x2_5.get_content(),
                         [['aa', 'aa', 'aa', 'aa'], [2, 2]],
                         "Error in operation, summation incorrect")
        # Two by two nummerical subtraction
        m_2x2_11 = a1_design.SymmetricMatrix([3, 2, 2, 3], [2, 2])
        m_2x2_12 = a1_design.SymmetricMatrix([2, 1, 1, 2], [2, 2])
        m_2x2_11.add_sub(m_2x2_2, True)
        self.assertEqual(m_2x2_1.get_content, [[1, 1, 1, 1], [2, 2]],
                         "Error in operation, addition incorrect")
        m_2x2_13 = a1_design.SymmetricMatrix([1, 2, 2, 1], [2, 2])
        m_2x2_14 = a1_design.SymmetricMatrix([0, 0, 0, 0], [2, 2])
        m_2x2_13.add_sub(m_2x2_14, True)
        self.assertEqual(m_2x2_3.get_content, [[1, 2, 2, 1], [2, 2]],
                         "Error in operation, addition incorrect")
        m_2x2_15 = a1_design.SymmetricMatrix([0, 0, 0, 0], [2, 2])
        m_2x2_16 = a1_design.SymmetricMatrix([1, 2, 2, 1], [2, 2])
        m_2x2_15.add_sub(m_2x2_16, True)
        self.assertEqual(m_2x2_15.get_content, [[-1, -2, -2, 1], [2, 2]],
                         "Error in operation, addition incorrect")
        m_2x2_17 = a1_design.SymmetricMatrix([1, 2, 2, 1], [2, 2])
        m_2x2_18 = a1_design.SymmetricMatrix([1, 2, 2, 1], [2, 2])
        m_2x2_17.add_sub(m_2x2_18, True)
        self.assertEqual(m_2x2_17.get_content, [[0, 0, 0, 0], [2, 2]],
                        "Error in operation, addition incorrect")
        m_2x2_19 = a1_design.SymmetricMatrix([-1, -2, -2, -1], [2, 2])
        m_2x2_20 = a1_design.SymmetricMatrix([1, 2, 2, 1], [2, 2])
        m_2x2_19.add_sub(m_2x2_20, True)
        self.assertEqual(m_2x2_19.get_content, [[0, 0, 0, 0], [2, 2]],
                        "Error in operation, addition incorrect")
        m_2x2_21 = a1_design.SymmetricMatrix([-1, -2, -2, -1], [2, 2])
        m_2x2_20 = a1_design.SymmetricMatrix([-1, -2, -2, -1], [2, 2])
        m_2x2_21.add_sub(m_2x2_20, True)
        self.assertEqual(m_2x2_19.get_content, [[-2, -4, -4, -2], [2, 2]],
                        "Error in operation, addition incorrect")

    def test_symm_m_transpose(self):
        m_1x1.transpose()
        m_1x1 = a1_design.Symmetric([1], [1, 1])
        self.assertEqual(m_1x1.get_content(), [[1], [1, 1]], "Error"
                         "in operation, one by one int tranposition failed.")
        txt_m_1x1.transpose()
        txt_m_1x1 = a1_design.Symmetric(['a'], [1, 1])
        self.assertEqual(txt_m_1x1.get_content(), [['a'], [1, 1]], 
                         "Error in operation, one by one int tranposition"
                         "failed.")
        # Transpose two by two matrix containing only integers
        m_2x2.transpose()
        m_2x2 = a1_design.Symmetric([1, 2, 2, 1], [2, 2])
        self.assertEqual(m_2x2.get_content(), [[1, 2, 2, 1]], [2, 2],
                         "Error in operation, two by two int tranposition"
                         "failed")
        # Transpose two by two matrix containing objects other than integers
        m_2x2.transpose()
        txt_m_2x2 = a1_design.Symmetric(['a', 'b', 'b', 'a'], [2, 2])
        self.assertEqual(txt_m_2x2.get_content(),
                         [['a', 'b', 'b', 'a']], "Error in operation, two by"
                         "two obj tranposition failed")

    def test_symm_m_multi(self):
        # Test matrix multiplication
        # Test multiplication with one by one matries
        m_1x1_1 = a1_design.Symmetric([0], [1, 1])
        m_1x1_2 = a1_design.Symmetric([1], [1, 1])        
        m_1x1_1.multi(m_1x1_2)
        self.assertEqual(m_1x1_1.get_content(), [[0], [1, 1]],
                         "Error in operation, multiplication with one by one"
                         "matrix failed")
        # Test multiplication with one by two matrix and two by one matrix
        m_1x1_3 = a1_design.Symmetric([2], [1, 1])
        m_1x1_4 = a1_design.Symmetric([2], [1, 1])        
        m_1x2_4.multi(m_1x1_4)
        self.assertEqual(m_1x2_3.get_content(), [[4], [1, 1]],
                         "Error in operation, multiplication with one by two"
                         "and two by one matrices failed")
        m_2x2_1 = a1_design.Symmetric([1, 2, 2, 1], [2, 2])
        m_2x2_2 = a1_design.Symmetric([3, 2, 2, 3], [2, 2])
        m_2x2_1.multi(m_1x2_2)
        self.assertEqual(m_2x2_1.get_content(), [[7, 8, 8, 7], [2, 2]],
                         "Error in operation, multiplcation with two by one"
                         "and one by two matrices failed")

    def test_symm_m_get_by_row_or_col(self):
        m_1x1_1 = a1_design.SymmetricMatrix([1], [1, 1])
        ret_val = m_1x1_1.get_by_row_or_col([1, 1], True)
        self.assertEqual(ret_val, 1, "Error in getter, failed to retrieve by"
                         "row in one by one matrix")
        m_1x1_2 = a1_design.SymmetricMatrix([1], [1, 1])
        ret_val = m_1x1_2.get_by_row_or_col([1, 1], False)
        self.assertEqual(ret_val, 1, "Error in getter, failed to retrieve by"
                         "column in one by one matrix")
        txt_m_1x1_1 = a1_design.SymmetricMatrix(['a'], [1, 1])
        ret_val = txt_m_1x1_1.get_by_row_or_col([1, 1], True)
        self.assertEqual(ret_val, 'a', "Error in getter, failed to retrieve by"
                         "row in one by one matrix")
        txt_m_1x1_2 = a1_design.SymmetricMatrix(['a'], [1, 1])
        ret_val = txt_m_1x1_2.get_by_row_or_col([1, 1], False)
        self.assertEqual(ret_val, 'a', "Error in getter, failed to retrieve by"
                         "column in one by one matrix")
       # Test getter by row on 2 by 2 (square) matrix
        m_2x2_1 = a1_design.SymmetricMatrix([1, 2, 2, 1], [2, 2])
        ret_val = m_2x2_1.get_by_row_or_col([1, 1], True)
        self.assertEqual(ret_val, 1, "Error in getter, failed to retrieve by"
                         "row")
        m_2x2_2 = a1_design.SymmetricMatrix([1, 2, 2, 1], [2, 2])
        ret_val = m_2x2_2.get_by_row_or_col([1, 2], True)
        self.assertEqual(ret_val, 2, "Error in getter, failed to retrieve by"
                         "row")
        m_2x2_3 = a1_design.SymmetricMatrix([1, 2, 2, 1], [2, 2])
        ret_val = m_2x2_3.get_by_row_or_col([2, 1], True)
        self.assertEqual(ret_val, 1, "Error in getter, failed to retrieve by"
                         "row")
        m_2x2_4 = a1_design.SymmetricMatrix([1, 2, 2, 1], [2, 2])
        ret_val = m_2x2_4.get_by_row_or_col([2, 2], True)
        self.assertEqual(ret_val, 2, "Error in getter, failed to retrieve by"
                         "row")
        m_2x2_5 = a1_design.SymmetricMatrix([1, 2, 2, 1], [2, 2])
        ret_val = m_2x2_5.get_by_row_or_col([1, 1], False)
        self.assertEqual(ret_val, 1, "Error in getter, failed to retrieve by"
                         "column")
        m_2x2_6 = a1_design.SymmetricMatrix([1, 2, 2, 1], [2, 2])
        ret_val = m_2x2_6.get_by_row_or_col([1, 2], False)
        self.assertEqual(ret_val, 2, "Error in getter, failed to retrieve by"
                         "column")
        m_2x2_7 = a1_design.SymmetricMatrix([1, 2, 2, 1], [2, 2])
        ret_val = m_2x2_7.get_by_row_or_col([2, 1], False)
        self.assertEqual(ret_val, 1, "Error in getter, failed to retrieve by"
                         "column")
        m_2x2_8 = a1_design.SymmetricMatrix([1, 2, 3, 4], [2, 2])
        ret_val = m_2x2_8.get_by_row_or_col([2, 2], False)
        self.assertEqual(ret_val, 2, "Error in getter, failed to retrieve by"
                         "column")        
        txt_m_2x2_1 = a1_design.SymmetricMatrix(['a', 'b', 'b', 'a'], [2, 2])
        ret_val = txt_m_2x2_1.get_by_row_or_col([1, 1], True)
        self.assertEqual(ret_val, 'a', "Error in getter, failed to retrieve by"
                         "row")
        txt_m_2x2_2 = a1_design.SymmetricMatrix(['a', 'b', 'b', 'a'], [2, 2])
        ret_val = txt_m_2x2_2.get_by_row_or_col([1, 2], True)
        self.assertEqual(ret_val, 'b', "Error in getter, failed to retrieve by"
                         "row")
        txt_m_2x2_3 = a1_design.SymmetricMatrix(['a', 'b', 'b', 'a'], [2, 2])
        ret_val = txt_m_2x2_3.get_by_row_or_col([2, 1], True)
        self.assertEqual(ret_val, 'a', "Error in getter, failed to retrieve by"
                         "row")
        txt_m_2x2_4 = a1_design.SymmetricMatrix(['a', 'b', 'b', 'a'], [2, 2])
        ret_val = txt_m_2x2_4.get_by_row_or_col([2, 2], True)
        self.assertEqual(ret_val, 'b', "Error in getter, failed to retrieve by"
                         "row")
        txt_m_2x2_5 = a1_design.SymmetricMatrix(['a', 'b', 'b', 'a'], [2, 2])
        ret_val = txt_m_2x2_5.get_by_row_or_col([1, 1], False)
        self.assertEqual(ret_val, 'a', "Error in getter, failed to retrieve by"
                         "column")
        txt_m_2x2_6 = a1_design.SymmetricMatrix(['a', 'b', 'b', 'a'], [2, 2])
        ret_val = txt_m_2x2.get_by_row_or_col([1, 2], False)
        self.assertEqual(ret_val, 'b', "Error in getter, failed to retrieve by"
                         "column")
        txt_m_2x2_7 = a1_design.SymmetricMatrix(['a', 'b', 'b', 'a'], [2, 2])
        ret_val = txt_m_2x2_7.get_by_row_or_col([2, 1], False)
        self.assertEqual(ret_val, 'b', "Error in getter, failed to retrieve by"
                         "column")
        txt_m_2x2_8 = a1_design.SymmetricMatrix(['a', 'b', 'b', 'a'], [2, 2])
        ret_val = txt_m_2x2_8.get_by_row_or_col([2, 2], False)
        self.assertEqual(ret_val, 'a', "Error in getter, failed to retrieve by"
                         "column")

    def test_symm_set_by_row_col(self):
        # Test setter by row on 1 by 1 matrix
        m_1x1_1 = a1_design.SymmetricMatrix([1], [1, 1])
        m_1x1_1.set_by_row_or_col(2, [1, 1], True)
        self.assertEqual(m_1x1_1.get_content(), [[2], [1, 1]],
                         "Error in setter, failed to set by"
                         "row in one by one matrix")
        m_1x1_2 = a1_design.SymmetricMatrix([1], [1, 1])
        m_1x1_2.set_by_row_or_col(2, [1, 1], False)
        self.assertEqual(m_1x1_2.get_content(), [[2], [1, 1]],
                         "Error in setter, failed to set by"
                         "column in one by one matrix")
        txt_m_1x1_1 = a1_design.SymmetricMatrix(['a'], [1, 1])
        txt_m_1x1_1.set_by_row_or_col('b', [1, 1], True)
        self.assertEqual(txt_m_1x1_1.get_content(), [['b'], [1, 1]],
                         "Error in setter, failed to set by"
                         "row in one by one matrix")
        txt_m_1x1_2 = a1_design.SymmetricMatrix(['a'], [1, 1])
        txt_m_1x1_2.set_by_row_or_col('b', [1, 1], False)
        self.assertEqual(txt_m_1x1_2.get_content(), [[2], [1, 1]],
                         "Error in setter, failed to set by"
                         "column in one by one matrix")
        # Test setter by row on 2 by 2 (square) matrix
        m_2x2_1 = a1_design.SymmetricMatrix([1, 2, 3, 4], [2, 2])
        m_2x2_1.set_by_row_or_col(7, [1, 1], True)
        self.assertEqual(m_2x2_1.get_content(),[[7, 2, 3, 4], [2, 2]],
                         "Error in setter, failed to retrieve by"
                         "row in two by two matrix")
        m_2x2_2 = a1_design.SymmetricMatrix([1, 2, 3, 4], [2, 2])
        m_2x2_2.set_by_row_or_col(7, [1, 2], True)
        self.assertEqual(m_2x2_2.get_content(),[[1, 2, 7, 4], [2, 2]],
                         "Error in setter, failed to retrieve by"
                         "row in two by two matrix")
        m_2x2_3 = a1_design.SymmetricMatrix([1, 2, 3, 4], [2, 2])
        m_2x2_3.set_by_row_or_col(7, [2, 1], True)
        self.assertEqual(m_2x2_3.get_content(),[[1, 7, 3, 4], [2, 2]],
                         "Error in setter, failed to retrieve by"
                         "row in two by two matrix")
        m_2x2_4 = a1_design.SymmetricMatrix([1, 2, 3, 4], [2, 2])
        m_2x2_4.set_by_row_or_col(7, [2, 2], True)
        self.assertEqual(m_2x2_4.get_content(),[[1, 2, 3, 4], [2, 2]],
                         "Error in setter, failed to retrieve by"
                         "row in two by two matrix")        
        m_2x2_5 = a1_design.SymmetricMatrix([1, 2, 3, 4], [2, 2])
        m_2x2_5.set_by_row_or_col(7, [1, 1], False)
        self.assertEqual(m_2x2_5.get_content(),[[7, 2, 3, 4], [2, 2]],
                         "Error in setter, failed to retrieve by"
                         "column in two by two matrix")
        m_2x2_6 = a1_design.SymmetricMatrix([1, 2, 3, 4], [2, 2])
        m_2x2_6.set_by_row_or_col(7, [1, 2], False)
        self.assertEqual(m_2x2_6.get_content(),[[1, 7, 3, 4], [2, 2]],
                         "Error in setter, failed to retrieve by"
                         "column in two by two matrix") 
        m_2x2_7 = a1_design.SymmetricMatrix([1, 2, 3, 4], [2, 2])
        m_2x2_7.set_by_row_or_col(7, [2, 1], False)        
        self.assertEqual(m_2x2_5.get_content(),[[1, 2, 7, 4], [2, 2]],
                         "Error in setter, failed to retrieve by"
                         "column in two by two matrix")
        m_2x2_8 = a1_design.SymmetricMatrix([1, 2, 3, 4], [2, 2])
        m_2x2_8.set_by_row_or_col(7, [2, 2], False)
        self.assertEqual(m_2x2_5.get_content(),[[1, 2, 3, 7], [2, 2]],
                         "Error in setter, failed to retrieve by"
                         "column in two by two matrix")
        # Test setter by row on 2 by 2 (square) matrix
        m_2x2_1 = a1_design.SymmetricMatrix(['a', 'b', 'c', 'd'], [2, 2])
        m_2x2_1.set_by_row_or_col('x', [1, 1], True)
        self.assertEqual(m_2x2_1.get_content(),[['x', 'b', 'c', 'd'], [2, 2]],
                         "Error in setter, failed to retrieve by"
                         "row in two by two matrix")
        m_2x2_2 = a1_design.SymmetricMatrix(['a', 'b', 'c', 'd'], [2, 2])
        m_2x2_2.set_by_row_or_col('x', [1, 2], True)
        self.assertEqual(m_2x2_2.get_content(),[['a', 'b', 'x', 'd'], [2, 2]],
                         "Error in setter, failed to retrieve by"
                         "row in two by two matrix")
        m_2x2_3 = a1_design.SymmetricMatrix(['a', 'b', 'c', 'd'], [2, 2])
        m_2x2_3.set_by_row_or_col('x', [2, 1], True)
        self.assertEqual(m_2x2_3.get_content(),[['a', 'x', 'c', 'd'], [2, 2]],
                         "Error in setter, failed to retrieve by"
                         "row in two by two matrix")
        m_2x2_4 = a1_design.SymmetricMatrix(['a', 'b', 'c', 'd'], [2, 2])
        m_2x2_4.set_by_row_or_col('x', [2, 2], True)
        self.assertEqual(m_2x2_4.get_content(),[['a', 'b', 'c', 'x'], [2, 2]],
                         "Error in setter, failed to retrieve by"
                         "row in two by two matrix")        
        m_2x2_5 = a1_design.SymmetricMatrix(['a', 'b', 'c', 'd'], [2, 2])
        m_2x2_5.set_by_row_or_col('x', [1, 1], False)
        self.assertEqual(m_2x2_5.get_content(),[['x', 'b', 'c', 'd'], [2, 2]],
                         "Error in setter, failed to retrieve by"
                         "column in two by two matrix")
        m_2x2_6 = a1_design.SymmetricMatrix(['a', 'b', 'c', 'd'], [2, 2])
        m_2x2_6.set_by_row_or_col('x', [1, 2], False)
        self.assertEqual(m_2x2_6.get_content(),[['a', 'x', 'c', 'd'], [2, 2]],
                         "Error in setter, failed to retrieve by"
                         "column in two by two matrix") 
        m_2x2_7 = a1_design.SymmetricMatrix(['a', 'b', 'c', 'd'], [2, 2])
        m_2x2_7.set_by_row_or_col('x', [2, 1], False)        
        self.assertEqual(m_2x2_5.get_content(),[['a', 'b', 'c', 'd'], [2, 2]],
                         "Error in setter, failed to retrieve by"
                         "column in two by two matrix")
        m_2x2_8 = a1_design.SymmetricMatrix(['a', 'b', 'c', 'd'], [2, 2])
        m_2x2_8.set_by_row_or_col('x', [2, 2], False)
        self.assertEqual(m_2x2_5.get_content(),[['a', 'b', 'c', 'd'], [2, 2]],
                         "Error in setter, failed to retrieve by"
                         "column in two by two matrix")

    def test_symm_m_get_determinant(self):
         # Test get determinant method (applicable to only 2 by 2 matrices)
        m_2x2_1 = a1_design.SymmetricMatrix([0, 0, 0, 0], [2, 2])
        deter = m_2x2_1.get_determinant()
        self.assertEqual(deter, 0, "Error in operation, failed to form"
                         "determinant")
        m_2x2_2 = a1_design.SymmetricMatrix([1, 2, 2, 1], [2, 2])
        deter = m_2x2_2.get_determinant()
        self.assertEqual(deter, -3, "Error in operation, failed to form"
                         "determinant")
        m_2x2_3 = a1_design.SymmetricMatrix([1, 1, 1, 1], [2, 2])
        deter = m_2x2_3.get_determinant()
        self.assertEqual(deter, 0, "Error in operation, failed to form"
                         "determinant")
        m_2x2_4 = a1_design.SymmetricMatrix([-1, -1, -1, -1], [2, 2])
        deter = m_2x2_4.get_determinant()
        self.assertEqual(deter, 0, "Error in operation, failed to form"
                         "determinant")
        

    def test_symm_m_get_by_diag(self):
        # Test getter by index at diagonal
        m_1x1_1 = a1_design.Symmetric([1], [1, 1])
        ret_val = m_1x1_1.get_by_diag(1)
        self.assertEqual(ret_val, 1, "Error in operation, failed to retrieve"
                         "by diagonal in the square matrix")
        txt_m_1x1_1 = a1_design.Symmetric(['a'], [1, 1])
        ret_val = txt_m_1x1_1.get_by_diag(1)
        self.assertEqual(ret_val, 'a', "Error in operation, failed to retrieve"
                         "by diagonal in the square matrix")       
        m_2x2_1 = a1_design.Symmetric([1, 2, 2, 1], [2, 2])
        ret_val = m_2x2_1.get_by_diag(1)
        self.assertEqual(ret_val, 1, "Error in operation, failed to retrieve"
                         "by diagonal in the square matrix")
        m_2x2_2 = a1_design.Symmetric([1, 2, 2, 1], [2, 2])
        ret_val = m_2x2_2.get_by_diag(2)
        self.assertEqual(ret_val, 1, "Error in operation, failed to retrieve"
                         "by diagonal in the square matrix")
        txt_m_2x2_1 = a1_design.Symmetric(['a', 'b', 'b', 'a'], [2, 2])
        ret_val = m_2x2_1.get_by_diag(1)
        self.assertEqual(ret_val, 'a', "Error in operation, failed to retrieve"
                         "by diagonal in the square matrix")        
        txt_m_2x2_2 = a1_design.Symmetric(['a', 'b', 'b', 'a'], [2, 2])
        ret_val = m_2x2_2.get_by_diag(2)
        self.assertEqual(ret_val, 'a', "Error in operation, failed to retrieve"
                         "by diagonal in the square matrix")

    def test_symm_m_set_by_row_or_col(self):
        # Test overwritten setter.
        m_2x2_1 = a1.design.SymmetricMatrix([1, 2, 2, 1], [2, 2])
        m_2x2_1.set_by_row_or_col(7, [1, 1], True)
        self.assertEqual(m_2x2_1.get_content(),
                         [[7, 2, 2, 7], [1, 1]],
                         "Error in setting, failed to set value in symmetric"
                         "matrix")
        m_2x2_2 = a1.design.SymmetricMatrix([1, 2, 2, 1], [2, 2])
        m_2x2_2.set_by_row_or_col(7, [2, 2], True)
        self.assertEqual(m_2x2_2.get_content(),
                         [[7, 2, 2, 7], [1, 1]],
                         "Error in setting, failed to set value in symmetric"
                         "matrix")
        m_2x2_3 = a1.design.SymmetricMatrix([1, 2, 2, 1], [2, 2])
        m_2x2_3.set_by_row_or_col(7, [1, 1], False)
        self.assertEqual(m_2x2.get_content(),
                         [[7, 2, 2, 7], [1, 1]],
                         "Error in setting, failed to set value in symmetric"
                         "matrix")
        m_2x2 = a1.design.SymmetricMatrix([1, 2, 2, 1], [2, 2])
        m_2x2.set_by_row_or_col(7, [2, 2], False)
        self.assertEqual(m_2x2.get_content(),
                         [[7, 2, 2, 7], [1, 1]],
                         "Error in setting, failed to set value in symmetric"
                         "matrix")

class TestIdentityMatrix(unittest.TestCase):
    def test_ident_m__init__(self):
        # Test overwritten init method of the identity matrix without
        # specifying a value for the diagonal
        three_three_matrix_1 = a1_design.SymmetricMatrix(3)
        self.assertTrue(type(three_three_matrix_1)==IdentityMatrix,
                         "Error in initializing diffault identity matrix")
        three_three_matrix_1 = a1_design.SymmetricMatrix(3, 1)
        self.assertTrue(type(three_three_matrix_1)==IdentityMatrix,
                         "Error in initializing diffault identity matrix")        
        three_three_matrix_2 = a1_design.SymmetricMatrix(3, 2)
        self.assertTrue(type(three_three_matrix_2)==IdentityMatrix,
                         "Error in initializing identity matrix")
        
    def test_ident_m_get_content(self):
        m_2x2 = a1_design.SymmetricMatrix(2)
        self.assertEqual(m_2x2.get_content(), [[2, 0, 0, 2], [2, 2]],
                         "Error in retrieval, failure to retrieve content of"
                         "two by two matrix containing integers")
        
    def test_ident_m_add_sub(self):
        m_2x2_1 = a1_design.SymmetricMatrix(2)
        m_2x2_2 = a1_design.SymmetricMatrix(2, 2)
        m_2x2_1.add_sub(m_2x2_2, True)
        self.assertEqual(m_2x2_1.get_content, [[3, 0, 0, 3], [2, 2]],
                        "Error in operation, summation incorrect")
        m_2x2_3 = a1_design.SymmetricMatrix(2)
        m_2x2_4 = a1_design.SymmetricMatrix(2, 2)
        m_2x2_3.add_sub(m_2x2_4, False)
        self.assertEqual(m_2x2_19.get_content, [[-1, 0, 0, -1], [2, 2]],
                        "Error in operation, subtraction incorrect")
    
    def test_ident_m_get_by_row_or_col(self):
        m_2x2_1 = a1_design.SymmetricMatrix(2)
        ret_val = txt_m_2x2_7.get_by_row_or_col([2, 1], True)
        self.assertEqual(ret_val, 1, "Error in getter, failed to retrieve by"
                         "column")
        txt_m_2x2_8 = a1_design.SymmetricMatrix(2)
        ret_val = txt_m_2x2_8.get_by_row_or_col([2, 1], False)
        self.assertEqual(ret_val, 1, "Error in getter, failed to retrieve by"
                         "column") 
        
    def test_ident_m_get_determinant(self):
        m_2x2_1 = a1_design.SymmetricMatrix(2)
        deter = m_2x2_1.get_determinant()
        self.assertEqual(deter, 1, "Error in operation, failed to form"
                         "determinant")

class TestIdentityMatrix(unittest.TestCase):
    def test_ident_m__init__(self):
        # Test overwritten init method of the identity matrix without
        # specifying a value for the diagonal
        three_three_matrix_1 = a1_design.IdentityMatrix(3)
        self.assertTrue(type(three_three_matrix_1)==IdentityMatrix,
                         "Error in initializing diffault identity matrix")
        three_three_matrix_1 = a1_design.IdentityMatrix(3, 1)
        self.assertTrue(type(three_three_matrix_1)==IdentityMatrix,
                         "Error in initializing diffault identity matrix")        
        three_three_matrix_2 = a1_design.IdentityMatrix(3, 2)
        self.assertTrue(type(three_three_matrix_2)==IdentityMatrix,
                         "Error in initializing identity matrix")
        
    def test_ident_m_get_content(self):
        m_2x2 = a1_design.IdentityMatrix(2)
        self.assertEqual(m_2x2.get_content(), [[2, 0, 0, 2], [2, 2]],
                         "Error in retrieval, failure to retrieve content of"
                         "two by two matrix containing integers")
        
    def test_ident_m_add_sub(self):
        m_2x2_1 = a1_design.IdentityMatrix(2)
        m_2x2_2 = a1_design.IdentityMatrix(2, 2)
        m_2x2_1.add_sub(m_2x2_2, True)
        self.assertEqual(m_2x2_1.get_content, [[3, 0, 0, 3], [2, 2]],
                        "Error in operation, summation incorrect")
        m_2x2_3 = a1_design.SquareMatrix(2)
        m_2x2_4 = a1_design.IdentityMatrix(2, 2)
        m_2x2_3.add_sub(m_2x2_4, False)
        self.assertEqual(m_2x2_19.get_content, [[-1, 0, 0, -1], [2, 2]],
                        "Error in operation, subtraction incorrect")
    
    def test_ident_m_get_by_row_or_col(self):
        m_2x2_1 = a1_design.IdentityMatrix(2)
        ret_val = txt_m_2x2_7.get_by_row_or_col([2, 1], True)
        self.assertEqual(ret_val, 1, "Error in getter, failed to retrieve by"
                         "column")
        txt_m_2x2_8 = a1_design.Matrix(2)
        ret_val = txt_m_2x2_8.get_by_row_or_col([2, 1], False)
        self.assertEqual(ret_val, 1, "Error in getter, failed to retrieve by"
                         "column") 
        
    def test_ident_m_get_determinant(self):
        m_2x2_1 = a1_design.IdentityMatrix(2)
        deter = m_2x2_1.get_determinant()
        self.assertEqual(deter, 1, "Error in operation, failed to form"
                         "determinant")        
        


class TestOneDMatrix(unittest.TestCase):
    def test_oned_m_init(self):
        m_1x1 = a1_design.OneDMatrix([7], [1, 1])
        self.assertTrue(type(m_1x1) == Matrix, "__init__ does not"
                        "create proper object type with int matrices: failed"
                        " to create 1x1 integer holding matrix.")
        txt_m_1x1 = a1_design.OneDMatrix(['a'], [1, 1])
        self.assertTrue(type(txt_m_1x1_2) == Matrix, 
                        "__init__ does not create proper object type with int"
                        "matrices: failed to create 1x1 string holding"
                        "matrix.")
        
        m_1x2 = a1_design.OneDMatrix([1, 2], [1, 2])
        self.assertTrue(type(m_1x2) == Matrix, "__init__ does not"
                        "create proper object type with int matrices: failed"
                        "to create 1x2 integer holding matrix.")
        txt_m_1x2 = a1_design.OneDMatrix(['a', 'b'], [1, 2])
        self.assertTrue(type(txt_m_1x2) == Matrix, "__init__ does not"
                        "create proper object type with int matrices: failed"
                        "to create 1x2 string holding matrix.")
        
        m_2x1 = a1_design.OneDMatrix([1, 2], [2, 1])
        self.assertTrue(type(m_1x2) == Matrix, "__init__ does not"
                        "create proper object type with int matrices: failed"
                        "to create 2x1 integer holding matrix.")
        txt_m_2x1 = a1_design.OneDMatrix(['a', 'b'], [2, 1])
        self.assertTrue(type(txt_m_1x2) == Matrix, "__init__ does not"
                        "create proper object type with int matrices: failed"
                        "to create 2x1 string holding matrix.")
    def test_oned_m_get_content(self):
        # Test getter method
        # One element matrices
        m_1x1 = a1_design.OneDMatrix([7], [1, 1])
        txt_m_1x1 = a1_design.OneDMatrix(['a'], [1, 1])
        # One by two matrices
        m_1x2 = a1_design.OneDMatrix([1, 2], [1, 2])
        txt_m_1x2 = a1_design.OneDMatrix(['a', 'b'], [1, 2])
        # Two by two (square) matrices that are neither symmetric nor parallel
        m_2x2 = a1_design.OneDMatrix([1, 2, 3, 4], [2, 2])
        txt_m_2x2 = a1_design.OneDMatrix(['a', 'b', 'c', 'd'], [2, 2])
        # Test getter on one by one matrix containing integer only
        self.assertEqual(m_1x1.get_content(), [[7], [1, 1]], "Error"
                         "in retrieval, failure to retrieve content"
                         "of one by one matrix containing integer")
        # Test getter on one by one matrix containing object other integer
        self.assertEqual(txt_m_1x1.get_content(),
                         [['a'], [1, 1]], "Error in retrieval, failure to"
                         "retrieve content of one by one matrix containing"
                         "objects other integers")
        # Test getter on one by two matrix containing integer only
        self.assertEqual(m_1x2.get_content(), [[1, 2], [1, 2]],
                         "Error in retrieval, failure to retrieve content of"
                         "one by two matrix containing integers")
        # Test getter on one by two matrix containing object other integer
        self.assertEqual(txt_m_1x2_1.get_content(),
                         [['a', 'b'], [1, 2]], "Error in retrieval, failure"
                         "to retrieve content of one by two matrix containing"
                         "objects other integers")
    def test_oned_m_add_sub(self):
        # One by one numerical summation
        m_1x1_1 = a1_design.OneDMatrix([7], [1, 1])
        m_1x1_2 = a1_design.OneDMatrix([7], [1, 1])
        m_1x1_1.add_sub(m_1x1_2, True)
        self.assertEqual(m_1x1_1.get_content(), [[14], [1, 1]],
                         "Error in operation, summation incorrect")
        m_1x1_3 = a1_design.OneDMatrix([0], [1, 1])
        m_1x1_4 = a1_design.OneDMatrix([0], [1, 1])
        m_1x1_3.add_sub(m_1x1_4, True)
        self.assertEqual(m_1x1_3.get_content(), [[0], [1, 1]],
                         "Error in operation, summation incorrect")
        m_1x1_5 = a1_design.OneDMatrix([7], [1, 1])
        m_1x1_6 = a1_design.OneDMatrix([5], [1, 1])
        m_1x1_5.add_sub(m_1x1_6, True)
        self.assertEqual(m_1x1_5.get_content(), [[12], [1, 1]],
                         "Error in operation, summation incorrect")
        m_1x1_7 = a1_design.OneDMatrix([-3], [1, 1])
        m_1x1_8 = a1_design.OneDMatrix([5], [1, 1])
        m_1x1_7.add_sub(m_1x1_8, True)
        self.assertEqual(m_1x1_7.get_content(), [[2], [1, 1]],
                         "Error in operation, summation incorrect")
        m_1x1_7 = a1_design.OneDMatrix([-2], [1, 1])
        m_1x1_8 = a1_design.OneDMatrix([-3], [1, 1])
        m_1x1_7.add_sub(m_1x1_8, True)
        self.assertEqual(m_1x1_7.get_content(), [[-5], [1, 1]],
                         "Error in operation, summation incorrect")        
        txt_m_1x1_1 = a1_design.OneDMatrix(['a'], [1, 1])
        txt_m_1x1_2 = a1_design.OneDMatrix(['b'], [1, 1])
        txt_m_1x1_1.add_sub(txt_m_1x1_2, True)
        self.assertEqual(m_1x1_1.get_content(), [['ab'], [1, 1]],
                         "Error in operation, summation incorrect")
        txt_m_1x1_3 = a1_design.OneDMatrix(['a'], [1, 1])
        txt_m_1x1_4 = a1_design.OneDMatrix(['a'], [1, 1])
        txt_m_1x1_3.add_sub(txt_m_1x1_4, True)
        self.assertEqual(m_1x1_3.get_content(), [['aa'], [1, 1]],
                         "Error in operation, summation incorrect")
        # One by one numerical subtraction
        m_1x1_9 = a1_design.OneDMatrix([7], [1, 1])
        m_1x1_10 = a1_design.OneDMatrix([7], [1, 1])
        m_1x1_9.add_sub(m_1x1_2, True)
        self.assertEqual(m_1x1_9.get_content(), [[0], [1, 1]],
                         "Error in operation, summation incorrect")
        m_1x1_11 = a1_design.OneDMatrix([0], [1, 1])
        m_1x1_12 = a1_design.OneDMatrix([0], [1, 1])
        m_1x1_11.add_sub(m_1x1_12, True)
        self.assertEqual(m_1x1_11.get_content(), [[0], [1, 1]],
                         "Error in operation, summation incorrect")
        m_1x1_13 = a1_design.OneDMatrix([7], [1, 1])
        m_1x1_14 = a1_design.OneDMatrix([5], [1, 1])
        m_1x1_13.add_sub(m_1x1_14, True)
        self.assertEqual(m_1x1_13.get_content(), [[2], [1, 1]],
                         "Error in operation, summation incorrect")
        m_1x1_15 = a1_design.OneDMatrix([-3], [1, 1])
        m_1x1_16 = a1_design.OneDMatrix([5], [1, 1])
        m_1x1_15.add_sub(m_1x1_16, True)
        self.assertEqual(m_1x1_15.get_content(), [[-8], [1, 1]],
                         "Error in operation, summation incorrect")
        m_1x1_17 = a1_design.OneDMatrix([-2], [1, 1])
        m_1x1_18 = a1_design.OneDMatrix([-3], [1, 1])
        m_1x1_17.add_sub(m_1x1_18, True)
        self.assertEqual(m_1x1_17.get_content(), [[1], [1, 1]],
                         "Error in operation, summation incorrect")      
        # One by two numerical summation
        m_1x2_1 = a1_design.OneDMatrix([1, 2], [1, 2])
        m_1x2_2 = a1_design.OneDMatrix([3, 4], [1, 2])
        m_1x2_1.add_sub(m_1x2_2, True)
        self.assertEqual(txt_m_1x1_1.get_content(), [[4, 6], [1, 2]],
                         "Error in operation, summation incorrect")
        m_1x2_3 = a1_design.OneDMatrix([1, 2], [1, 2])
        m_1x2_4 = a1_design.OneDMatrix([1, 2], [1, 2])
        m_1x2_3.add_sub(m_1x2_4, True)
        self.assertEqual(txt_m_1x1_3.get_content(), [[2, 4], [1, 2]],
                         "Error in operation, summation incorrect")
        m_1x2_5 = a1_design.OneDMatrix([0, 0], [1, 2])
        m_1x2_6 = a1_design.OneDMatrix([0, 0], [1, 2])
        m_1x2_5.add_sub(m_1x2_6, True)
        self.assertEqual(txt_m_1x1_5.get_content(), [[0, 0], [1, 2]],
                         "Error in operation, summation incorrect")
        m_1x2_7 = a1_design.OneDMatrix([5, 7], [1, 2])
        m_1x2_8 = a1_design.OneDMatrix([-3, -2], [1, 2])
        m_1x2_7.add_sub(m_1x2_8, True)
        self.assertEqual(txt_m_1x1_7.get_content(), [[2, 5], [1, 2]],
                         "Error in operation, summation incorrect")
        m_1x2_9 = a1_design.OneDMatrix([-5, -7], [1, 2])
        m_1x2_10 = a1_design.OneDMatrix([3, 2], [1, 2])
        m_1x2_9.add_sub(m_1x2_10, True)
        self.assertEqual(txt_m_1x1_9.get_content(), [[-2, -5], [1, 2]],
                         "Error in operation, summation incorrect")
        m_1x2_11 = a1_design.OneDMatrix([-5, -7], [1, 2])
        m_1x2_12 = a1_design.OneDMatrix([-3, -2], [1, 2])
        m_1x2_11.add_sub(m_1x2_10, True)
        self.assertEqual(txt_m_1x1_9.get_content(), [[-8, -9], [1, 2]],
                         "Error in operation, summation incorrect")
        # One by two string summation   
        txt_m_1x2_1 = a1_design.OneDMatrix(['a', 'b'], [1, 2])
        txt_m_1x2_2 = a1_design.OneDMatrix(['c', 'd'], [1, 2])
        txt_m_1x2_1.add_sub(m_1x2_2, True)
        self.assertEqual(txt_m_1x1_1.get_content(), [['ac', 'bd'], [1, 2]],
                         "Error in operation, summation incorrect")
        txt_m_1x2_1 = a1_design.OneDMatrix(['a', 'a'], [1, 2])
        txt_m_1x2_2 = a1_design.OneDMatrix(['c', 'c'], [1, 2])
        txt_m_1x2_1.add_sub(m_1x2_2, True)
        self.assertEqual(txt_m_1x1_1.get_content(), [['ac', 'ac'], [1, 2]],
                         "Error in operation, summation incorrect")
        # One by two subtraction
        m_1x2_11 = a1_design.OneDMatrix([3, 4], [1, 2])
        m_1x2_12 = a1_design.OneDMatrix([1, 2], [1, 2])
        m_1x2_1.add_sub(m_1x2_12, False)
        self.assertEqual(txt_m_1x1_11.get_content(), [[2, 4], [1, 2]],
                         "Error in operation, subtracton incorrect")
        m_1x2_13 = a1_design.OneDMatrix([1, 2], [1, 2])
        m_1x2_14 = a1_design.OneDMatrix([1, 2], [1, 2])
        m_1x2_13.add_sub(m_1x2_14, True)
        self.assertEqual(txt_m_1x1_13.get_content(), [[0, 0], [0, 0]],
                         "Error in operation, subtraction incorrect")
        m_1x2_15 = a1_design.OneDMatrix([0, 0], [1, 2])
        m_1x2_16 = a1_design.OneDMatrix([0, 0], [1, 2])
        m_1x2_15.add_sub(m_1x2_15, True)
        self.assertEqual(txt_m_1x1_1.get_content(), [[0, 0], [1, 2]],
                         "Error in operation, subtraction incorrect")
        m_1x2_17 = a1_design.OneDMatrix([5, 7], [1, 2])
        m_1x2_18 = a1_design.OneDMatrix([-3, -2], [1, 2])
        m_1x2_17.add_sub(m_1x2_18, True)
        self.assertEqual(txt_m_1x2_17.get_content(), [[2, 5], [1, 2]],
                         "Error in operation, subtracion incorrect")
        m_1x2_19 = a1_design.OneDMatrix([-5, -7], [1, 2])
        m_1x2_20 = a1_design.OneDMatrix([3, 2], [1, 2])
        m_1x2_19.add_sub(m_1x2_20, True)
        self.assertEqual(txt_m_1x1_19.get_content(), [[-8, -9], [1, 2]],
                         "Error in operation, subtraction incorrect")
        m_1x2_21 = a1_design.OneDMatrix([-5, -7], [1, 2])
        m_1x2_22 = a1_design.OneDMatrix([-3, -2], [1, 2])
        m_1x2_21.add_sub(m_1x2_22, True)
        self.assertEqual(txt_m_1x1_21.get_content(), [[-2, -5], [1, 2]],
                         "Error in operation, subtraction incorrect")
        # Two by one numerical summation
        m_2x1_1 = a1_design.OneDMatrix([1, 2], [2, 1])
        m_2x1_2 = a1_design.OneDMatrix([3, 4], [2, 1])
        m_2x1_1.add_sub(m_2x1_2, True)
        self.assertEqual(txt_m_2x1_1.get_content(), [[4, 6], [2, 1]],
                         "Error in operation, addition incorrect")
        m_2x1_3 = a1_design.OneDMatrix([0, 0], [2, 1])
        m_2x1_4 = a1_design.OneDMatrix([0, 0], [2, 1])
        m_2x1_3.add_sub(m_2x1_4, True)
        self.assertEqual(txt_m_2x1_1.get_content(), [[0, 0], [2, 1]],
                         "Error in operation, addition incorrect")
        m_2x1_5 = a1_design.OneDMatrix([1, 2], [2, 1])
        m_2x1_6 = a1_design.OneDMatrix([-4, -2], [2, 1])
        m_2x1_5.add_sub(m_2x1_6, True)
        self.assertEqual(txt_m_2x1_5.get_content(), [[-3, 0], [2, 1]],
                         "Error in operation, addition incorrect")
        m_2x1_7 = a1_design.OneDMatrix([-4, -2], [2, 1])
        m_2x1_8 = a1_design.OneDMatrix([-1, -3], [2, 1])
        m_2x1_7.add_sub(m_2x1_8, True)
        self.assertEqual(txt_m_2x1_7.get_content(), [[-5, -5], [2, 1]],
                         "Error in operation, addition incorrect")
        # Two by one string summation
        txt_m_2x1_1 = a1_design.OneDMatrix(['a', 'b'], [2, 1])
        txt_m_2x1_2 = a1_design.OneDMatrix(['c', 'd'], [2, 1])
        txt_m_2x1_1.add_sub(txt_m_2x1_2, True)
        self.assertEqual(txt_m_2x1_1.get_content(), [['ac', 'bd'], [2, 1]],
                         "Error in operation, addition incorrect")
        txt_m_2x1_3 = a1_design.OneDMatrix(['a', 'a'], [2, 1])
        txt_m_2x1_4 = a1_design.OneDMatrix(['a', 'a'], [2, 1])
        txt_m_2x1_3.add_sub(txt_m_2x1_4, True)
        self.assertEqual(txt_m_2x1_1.get_content(), [['aa', 'aa'], [2, 1]],
                         "Error in operation, addition incorrect")
        txt_m_2x1_3 = a1_design.OneDMatrix(['a', 'b'], [2, 1])
        txt_m_2x1_4 = a1_design.OneDMatrix(['a', 'b'], [2, 1])
        txt_m_2x1_3.add_sub(txt_m_2x1_4, True)
        self.assertEqual(txt_m_2x1_1.get_content(), [['aa', 'bb'], [2, 1]],
                         "Error in operation, addition incorrect")
        # Two by one numerical subtraction
        m_2x1_9 = a1_design.OneDMatrix([3, 4], [2, 1])
        m_2x1_10 = a1_design.OneDMatrix([1, 2], [2, 1])
        m_2x1_9.add_sub(m_2x1_10, True)
        self.assertEqual(txt_m_2x1_9.get_content(), [[2, 2], [2, 1]],
                         "Error in operation, subtraction incorrect")
        m_2x1_11 = a1_design.OneDMatrix([0, 0], [2, 1])
        m_2x1_12 = a1_design.OneDMatrix([0, 0], [2, 1])
        m_2x1_11.add_sub(m_2x1_12, True)
        self.assertEqual(txt_m_2x1_1.get_content(), [[0, 0], [2, 1]],
                         "Error in operation, subtraction incorrect")
        m_2x1_13 = a1_design.OneDMatrix([1, 2], [2, 1])
        m_2x1_14 = a1_design.OneDMatrix([-4, -2], [2, 1])
        m_2x1_13.add_sub(m_2x1_14, True)
        self.assertEqual(txt_m_2x1_13.get_content(), [[5, 0], [2, 1]],
                         "Error in operation, subtraction incorrect")
        m_2x1_15 = a1_design.OneDMatrix([-4, -2], [2, 1])
        m_2x1_16 = a1_design.OneDMatrix([-1, -3], [2, 1])
        m_2x1_15.add_sub(m_2x1_16, True)
        self.assertEqual(txt_m_2x1_7.get_content(), [[-3, 1], [2, 1]],
                         "Error in operation, subtracion incorrect")
    
    def test_oned_m_transpose(self):
        # Test the transpose method
        # One by one matrices
        m_1x1 = a1.design.OneDMatrix([1], [1, 1])
        txt_m_1x1 = a1.design.OneDMatrix(['a'], [1, 1])
        # One by two matrices
        m_1x2 = a1_design.OneDMatrix([1, 2], [1, 2])
        txt_m_1x2 = a1_design.OneDMatrix(['a', 'b'], [1, 2])
        # Two by one matrices
        m_2x1_1 = a1_design.OneDMatrix([1, 2], [2, 1])
        txt_m_2x1 = a1_design.OneDMatrix(['a', 'b'], [2, 1])
        # Two by two (square) matrices that are neither symmetric nor parallel
        m_2x2 = a1_design.OneDMatrix([1, 2, 3, 4], [2, 2])
        txt_m_2x2 = a1_design.OneDMatrix(['a', 'b', 'c', 'd'], [2, 2])
        m_1x1.tranpose()
        self.assertEqual(m_1x1.get_content(), [[1], [1, 1]], "Error in"
                         "operation, one by one int tranposition failed")
        txt_m_1x1.transpose()
        self.assertEqual(txt_m_1x1.get_content(), [['a'], [1, 1]], "Error in"
                         "operation, one by one string transposition failed")
        # Transpose one by two matrix containing integers only
        m_1x2.transpose()
        self.assertEqual(m_1x2.get_content(), [[1, 2], [2, 1]],
                         "Error in operation, one by two int transposition"
                         "failed")
        # Transpose one by two matrix containing objects other than integers
        txt_m_1x2.transpose()
        self.assertEqual(txt_two_matrix.get_content(), [['a', 'b'], [2, 1]],
                         "Error in operation, one by two obj tranposition"
                         "failed")
        # Transpose two by one matrix containing integers only
        m_2x1.transpose()
        self.assertEqual(m_2x1.get_content(), [[1, 2], [1, 2]],
                         "Error in operation, two by one int tranposition"
                         "failed")
        # Transpose two by one matrix containing objects other than integers
        txt_m_2x1.transpose()
        self.assertEqual(txt_m_2x1.get_content(), ['a', 'b'], [1, 2],
                         "Error in operation, two by one obj transpoition"
                         "failed")
    
    def test_oned_m_multi(self):
        # Test matrix multiplication
        # One element matrices
        m_1x1_1 = a1_design.OneDMatrix([7], [1, 1])
        m_1x1_2 = a1_design.OneDMatrix([5], [1, 1])
        # One by two matrices
        m_1x2_1 = a1_design.OneDMatrix([1, 2], [1, 2])
        m_1x2_2 = a1_design.OneDMatrix([1, 2], [1, 2])
        # Two by one matrices
        m_2x1 = a1_design.OneDMatrix([3, 4], [2, 1])
        # Two by two (square) matrices that are neither symmetric nor parallel
        m_2x2_1 = a1_design.OneDMatrix([1, 2, 3, 4], [2, 2])
        m_2x2_1 = a1_design.OneDMatrix([5, 6, 7, 8], [2, 2])
        # Test multiplication with one by one matries
        m_1x1_1.multi(m_1x1_2)
        self.assertEqual(m_1x1_1.get_content(), [[35], [1, 1]],
                         "Error in operation, multiplication with one by one"
                         "matrix failed")
        # Test multiplication with one by two matrix and two by one matrix
        m_1x2_1.multi(m_2x1)
        self.assertEqual(m_1x2_1.get_content(), [[5], [1, 1]],
                         "Error in operation, multiplication with one by two"
                         "and two by one matrices failed")
    def test_oned_m_switch(self):
        # Test column/row switching
        m_1x1 = a1_design.OneDMatrix([1], [1, 1])
        m_1x1.switch(True, [1, 1])
        self.assertEqual(m_1x1.get_content(), [[1], [1, 1]],
                         "Error in operation, failure to switch rows")
        m_1x1.switch(False, [1, 1])
        self.assertEqual(m_1x1.get_content(), [[1], [1, 1]],
                         "Error in operation, failure to switch columns")
        txt_m_1x1 = a1_design.OneDMatrix(['a'], [1, 1])
        txt_m_1x1.switch(True, [1, 1])
        self.assertEqual(txt_m_1x1.get_content(), [['a'], [1, 1]],
                         "Error in operation, failure to switch rows")
        txt_m_1x1.switch(False, [1, 1])
        self.assertEqual(txt_m_1x1.get_content(), [['a'], [1, 1]],
                         "Error in operation, failure to switch columns")      
        m_1x2 = a1.design.OneDMatrix([1, 2], [1, 2])
        m_1x2.switch(True, [1, 2])
        self.assertEqual(m_2x2.get_content(), [[2, 1], [1, 2]],
                         "Error in operation, failure to switch rows")
        m_1x2 = a1.design.OneDMatrix([1, 2], [1, 2])
        m_1x2.switch(False, [1, 1])
        self.assertEqual(m_1x2.get_content(), [[1, 2], [1, 2]],
                         "Error in operation, failure to switch rows")
        m_1x2 = a1.design.OneDMatrix(['a', 'b'], [1, 2])
        m_1x2.switch(True, [1, 2])
        self.assertEqual(m_2x2.get_content(), [['b', 'a'], [1, 2]],
                         "Error in operation, failure to switch rows")
        m_1x2 = a1.design.OneDMatrix(['a', 'b'], [1, 2])
        m_1x2.switch(False, [1, 1])
        self.assertEqual(m_1x2.get_content(), [['a', 'b'], [1, 2]],
                         "Error in operation, failure to switch rows")        
        m_2x1 = a1.design.OneDMatrix([1, 2], [2, 1])
        m_2x1.switch(True, [2, 1])
        self.assertEqual(m_2x1.get_content(), [[2, 1], [2, 1]],
                         "Error in operation, failure to switch columns")
        m_2x1 = a1.design.OneDMatrix([1, 2], [2, 1])
        m_2x1.switch(False, [2, 1])
        self.assertEqual(m_2x2.get_content(), [[1, 2], [2, 1]],
                         "Error in operation, failure to switch columns")        
        m_2x1 = a1.design.OneDMatrix(['a', 'b'], [2, 1])
        m_2x1.switch(True, [2, 1])
        self.assertEqual(m_2x1.get_content(), [['b', 'a'], [2, 1]],
                         "Error in operation, failure to switch columns")
        m_2x1 = a1.design.OneDMatrix(['a', 'b'], [2, 1])
        m_2x1.switch(False, [2, 1])
        self.assertEqual(m_2x2.get_content(), [['a', 'b'], [2, 1]],
                         "Error in operation, failure to switch columns")

    def test_get_val(self):
        # Test getter method which retrieves by index of a row matrix
        row_matrix = a1_design.OneDMatrix([1, 2, 3, 4], [1, 4])
        ret_val = row_matrix.get_val(3)
        self.assertEqual(ret_val, 3, "Error in retrieval, failure to retrieve"
                         "value by index in row matrix")

        # Test getter method which retrieves by index of a column matrix
        column_matrix = a1_design.OneDMatrix([1, 2, 3, 4], [4, 1])
        ret_val = column_matrix.get_val(3)
        self.assertEqual(ret_val, 3, "Error in retrieval, failure to retrieve"
                         "value by index in column matrix")
        
    def test_set_val(self):
        # Test setter method which sets by index of a row matrix
        row_matrix = a1_design.OneDMatrix([1, 2, 3, 4], [1, 4])
        row_matrix.set_val(2, 7)
        self.assertEqual(row_matrix.get_content(), [[1, 7, 3, 4], [1, 4]],
                         "Error in setting, failure to set value in row"
                         "matrix by index")
        # Test setter method which sets by index of a column matrix
        column_matrix = a1_designt.OneDMatrix([1, 2, 3, 4], [4, 1])
        column_matrix.set_val(2, 7)
        self.assertEqual(column_matrix.get_content(), [[1, 7, 3, 4], [4, 1]],
                         "Error in setting, failure to set value in column"
                         "matrix by index")





