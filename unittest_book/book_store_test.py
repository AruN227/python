import unittest
from book_store import calculate_total

class BookStoreTest(unittest.TestCase):
    def test_only_single_book(self):
        self.assertEqual(calculate_total([1]),800)

    def test_two_of_the_same_book(self):
        self.assertEqual(calculate_total([2, 2]), 1600)

    def test_two_groups_of_4_is_cheaper_than_group_of_5_plus_group_of_3(self):
        self.assertEqual(calculate_total([1, 1, 2, 2, 3, 3, 4, 5]), 3800)

    def test_group_of_4_plus_group_of_2_is_cheaper_than_2_groups_of_3(self):
        self.assertEqual(calculate_total([1, 1, 2, 2, 3, 4]), 3500)


if __name__ == "__main__":
    unittest.main()
