import unittest
from insertion_sort import insertion_sort

class InsertionSortTestCase(unittest.TestCase):
    """Tests for insertion sort."""

    def test_unordered_list(self):
        """Test if the insertion sort works in an unordered list."""
        list = [25, 34, 98, 7, 41, 19, 5]
        insertion_sort(list)
        self.assertEqual([5, 7, 19, 25, 34, 41, 98], list)

    def test_semiordered_list(self):
        """Test if the algorithm works in a semiordered list."""
        list = [43, 21, 19, 59, 62, 79]
        insertion_sort(list)
        self.assertEqual([19, 21, 43, 59, 62, 79], list)

    def test_single_element_list(self):
        """Test if the insertion sort works in a list with a single element."""
        list = [5]
        insertion_sort(list)
        self.assertEqual([5], list)


if __name__ == '__main__':
    unittest.main()
