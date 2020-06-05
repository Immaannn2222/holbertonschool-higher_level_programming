#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def testA(self):
        """Standard"""
        llist = [1, 2, 3]
        self.assertEqual(3, max_integer(llist))

    def testA(self):
        """at the beginning"""
        llist = [5, 2, 3]
        self.assertEqual(5, max_integer(llist))

    def testB(self):
        """negative integers and zero"""
        llist = [-14751, 0, -12, -13]
        self.assertEqual(0, max_integer(llist))

    def testempty(self):
        """empty case"""
        self.assertEqual(None, max_integer())

    def single_list(self):
        """1 element"""
        llist = [1]
        self.assertEqual(1, max_integer(llist))

    def float_list(self):
        """list conatins float"""
        llist = [12, 13.5, 0.259, 1, -128, 1478]
        with self.assertRaises(TypeError):
            max_integer(None)

    def large_list(self):
        """large list"""
        llist = [125, 12, -124, 11457, -147, 120, 158, 13, 1, 5, 8, 9, 11, 2]
        self.assertEqual(11475, max_integer(llist))

    def test_none2(self):
        """none v2"""
        with self.assertRaises(TypeError):
            max_integer(None)

    def All_negative(self):
        """negative"""
        llist_n = [-1, -2, -3]
        self.assertEqual(-1, max_integer(llist_n))

    def tests_max_str(self):
        """integers"""
        self.assertEqual(max_integer("fzk"), 'z')


if __name__ == '__main__':
    unittest.main()
