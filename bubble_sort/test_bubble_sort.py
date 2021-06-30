import unittest
from bubble_sort import bubble_sort

class BubbleSortTestCase(unittest.TestCase):
    """Tests for the bubble sort."""

    def test_unordered_list(self):
        """Test if the bubble sort works in an unordered list."""
        list = [25, 34, 98, 7, 41, 19, 5]
        bubble_sort(list)
        self.assertEqual([5, 7, 19, 25, 34, 41, 98], list)


if __name__ == '__main__':
    unittest.main()
