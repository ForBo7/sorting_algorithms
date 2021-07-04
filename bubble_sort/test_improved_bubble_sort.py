import unittest
from improved_bubble_sort import improved_bubble_sort


class ImprovedBubbleSortTestCase(unittest.TestCase):
    """Tests for the improved bubble sort."""

    def test_unordered_list(self):
        """Test if the algorithm works with an unordered list."""
        list = [25, 34, 98, 7, 41, 19, 5]
        improved_bubble_sort(list)
        self.assertEqual([5, 7, 19, 25, 34, 41, 98], list)

    def test_semiordered_list(self):
        """Test if the algorithm works in a semiordered list."""
        list = [43, 21, 19, 59, 62, 79]
        improved_bubble_sort(list)
        self.assertEqual([19, 21, 43, 59, 62, 79], list)

    def test_single_element_list(self):
        """Test if the bubble sort works in a list with a single element."""
        list = [5]
        improved_bubble_sort(list)
        self.assertEqual([5], list)

    def test_repeating_element_list(self):
        """
        Test if the bubble sort works in a list with repeating elements.
        """
        list = [4, 4, 1, 9, 3, 3, 3, 2]
        improved_bubble_sort(list)
        self.assertEqual([1, 2, 3, 3, 3, 4, 4, 9], list)


if __name__ == '__main__':
    unittest.main()
