import unittest
import sys
sys.path.append('.')

from logic import *
from testfixtures import should_raise

class TestLongestSeq(unittest.TestCase):
    def test_correct_created(self):
        created_matrix = create_matrix_from_file(f'tests/test_1')
        expected = [["R", "R", "B"], ["G", "G", "R"], ["R", "B", "G"]]
        self.assertEqual(created_matrix, expected)

    @should_raise(ValueError)
    def test_wrong_input(self):
        created_matrix = create_matrix_from_file(f'tests/test_wrong_input')

    @should_raise(ValueError)
    def test_wrong_letter_input(self):
        created_matrix = create_matrix_from_file(f'tests/test_wrong_input_2')


if __name__ == '__main__':
    unittest.main()
