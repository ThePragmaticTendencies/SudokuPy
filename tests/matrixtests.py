import unittest
from matrix import Matrix

class MatrixTests(unittest.TestCase):
    def setUp(self):
        """
        How is matrix composed?
        Collection of:      |0, 2, 0,  3, 0, 4,  8, 9, 1,  0, 0, 0,  0, 0, 0,  0, 0, 7,  0, 0, 0,  0, 0, 0,  0, 0, 0,  0, 0, 0,  1, 0, 0,  6, 0, 8|
        Transforms into:    | 0, 2, 0, | 3, 0, 4, | 8, 9, 1, | 0, 0, 0, | 0, 0, 0, | 0, 0, 7, | 0, 0, 0, | 0, 0, 0, | 0, 0, 0, | 0, 0, 0, | 1, 0, 0, | 6, 0, 8 |

        and into:           | 0, 2, 0, | 3, 0, 4, |
                            | 8, 9, 1, | 0, 0, 0, |
                            | 0, 0, 0, | 0, 0, 7, |

                            | 0, 0, 0, | 0, 0, 0, |
                            | 0, 0, 0, | 0, 0, 0, |
                            | 1, 0, 0, | 6, 0, 8  |
        so we take dim * number of cells, row by row
        """
        self.matrix = Matrix(3, 2, [0, 2, 0,  3, 0, 4,  8, 9, 1,  0, 0, 0,  0, 0, 0,  0, 0, 7,  0, 0, 0,  0, 0, 0,  0, 0, 0,  0, 0, 0,  1, 0, 0,  6, 0, 8])

    def test_invalid_matrix_dim_exception(self):
        self.assertRaises(ValueError, lambda: Matrix(3, 3, [1,2,3]).get())

    def test_numbers_in_cells(self):
        self.assertEqual(self.matrix.numbersInCells(), [[2, 8, 9, 1], [3, 4, 7], [1], [6, 8]])
    
    def test_cell_number_at_row_and_position(self):
        self.assertEqual(self.matrix._cellNumber(1, 1), 0)
        self.assertEqual(self.matrix._cellNumber(1, 3), 1)
        self.assertEqual(self.matrix._cellNumber(1, 5), 1)
        self.assertEqual(self.matrix._cellNumber(2, 1), 0)
        self.assertEqual(self.matrix._cellNumber(3, 0), 2)
        self.assertEqual(self.matrix._cellNumber(5, 5), 3)
    
    def test_cells_by_rows(self):
        self.assertEqual(self.matrix.cellsByRows(), [[0, 1], [0, 1], [0, 1], [2, 3], [2, 3], [2, 3]])

    def test_cells_by_columns(self):
        self.assertEqual(self.matrix.cellsByColumns(), [[0, 2], [0, 2], [0, 2], [1, 3],  [1, 3],  [1, 3]])
    
    def test_potentials_in_rows(self):
        self.assertEqual(self.matrix.potentialsInDirection('row'), [[0, 2, 4], [3, 4, 5], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4, 5],  [0, 1, 2, 3, 4, 5],  [1, 2, 4]])
    
    def test_potentials_in_columns(self):
        self.assertEqual(self.matrix.potentialsInDirection('column'), [[0, 2, 3, 4], [2, 3, 4, 5], [0, 2, 3, 4, 5], [1, 2, 3, 4],  [0, 1, 2, 3, 4, 5],  [1, 3, 4]])

    def test_numbers_in_rows(self):
        self.assertEqual(self.matrix.numbersInDirection('row'), [[2, 3, 4], [8, 9, 1], [7], [],  [],  [1, 6, 8]])

    def test_numbers_in_columns(self):
        self.assertEqual(self.matrix.numbersInDirection('column'), [[8, 1], [2, 9], [1], [3, 6],  [],  [4, 7, 8]])

if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)