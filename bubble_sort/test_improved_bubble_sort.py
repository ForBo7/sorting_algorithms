import unittest
from improved_bubble_sort import improved_bubble_sort


class ImprovedBubbleSortTestCase(unittest.TestCase):
    """Tests for the improved bubble sort."""

    def test_unordered_list(self):
        """Test if the algorithm works with an unordered list."""
        list = [25, 34, 98, 7, 41, 19, 5]
        improved_bubble_sort(list)
        self.assertEqual([5, 7, 19, 25, 34, 41, 98], list)


if __name__ == '__main__':
    unittest.main()
