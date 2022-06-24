import unittest
from unittest import TestCase
from Agile_7 import Word_P


class TestAgile_7(TestCase):

    def setUp(self):
        self.Word_P = Word_P()

    def test_reverse(self):
        self.assertEqual(self.Word_P.reverse('абырвалг'), 'главрыба')

if __name__ == "__main__":
    unittest.main()
