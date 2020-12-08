#!/usr/bin/env python3


import unittest

import inode_alloc
import inode_math


class TestCheckINodeMath(unittest.TestCase):

    def test_small(self):
        n = 5
        self.assertEqual(inode_alloc.find_index_blocks(n), inode_math.find_index_blocks_math(n))

    def test_medium(self):
        n = 16
        self.assertEqual(inode_alloc.find_index_blocks(n), inode_math.find_index_blocks_math(n))

    def test_large(self):
        n = 50
        self.assertEqual(inode_alloc.find_index_blocks(n), inode_math.find_index_blocks_math(n))

    def test_xlarge(self):
        n = 2000
        self.assertEqual(inode_alloc.find_index_blocks(n), inode_math.find_index_blocks_math(n))

    def test_xxlarge(self):
        n = 20000
        self.assertEqual(inode_alloc.find_index_blocks(n), inode_math.find_index_blocks_math(n))


if __name__ == '__main__':
    unittest.main()

